# -*- coding: utf-8 -*-

from openerp import models, fields, api

class miembro(models.Model):
    _name = 'gym.miembro'

    name = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Email", required=True)
    direccion = fields.Text(string="Dirección", required=True)
    facturar = fields.Boolean(String="¿Requiere factura?")
    RFC = fields.Many2one('gym.rfc')
    tipo_miembro = fields.Many2one('gym.tipo_miembro')

    @api.onchange('facturar')
    def check_change(self):
        if self.facturar == False:
            self.RFC = None

class tipo_miembro(models.Model):
    _name = 'gym.tipo_miembro'
    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    

class rfc(models.Model):
    _name = 'gym.rfc'

    name = fields.Char(string="RFC", required=True)
    razon = fields.Char(string="Nombre o razón social", required=True)
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email", required=True)
    direccion = fields.Text(string="Dirección", required=True)

class suscripcion(models.Model):
    _name = "gym.suscripcion"
    
    miembro = fields.Many2one('gym.miembro', required=True, ondelete='cascade')
    tipo_suscripcion = fields.Many2one('gym.tipo_suscripcion', required=True)
    pago=fields.Many2many('gym.pago')
    inicio = fields.Date(string="Fecha de inicio", required=True)
    fin = fields.Date(string="Fecha de fin", compute='set_fin')
    monto = fields.Float(string="cantidad")
    abonado = fields.Float(string="abonado")
    uid_transaccion=fields.Char(compute='uid_transaccion_value')
    
    var_tipo_pago=fields.Many2one('gym.tipo_pago')
    var_cantidad=fields.Float()
    var_abonado=fields.Float()
        
    def uid_transaccion_value(self):
        if self.uid_transaccion == "":
            import uuid
            var = uuid.uuid4()
            self.uid_transaccion=str(var)
        else:
            self.uid_transaccion=self.uid_transaccion
        
    def set_fin(self):
        self.fin=self.inicio
        
    @api.onchange('tipo_suscripcion','pago')
    def actualizar_monto(self):
        self.monto=self.tipo_suscripcion.costo
        var = 0.0
        for x in self.pago:
            var = var + x.cantidad
        self.abonado=var
        

    @api.one
    def button_agregar_pago_parcial(self):
        sql="insert into gym_pago(tipo_pago,cantidad) VALUES(" + str(self.var_tipo_pago.id) + "," + str(self.var_cantidad) + ") RETURNING id"
        self.env.cr.execute(sql)
        pago_id= self.env.cr.fetchone()[0]
        self.env.cr.commit()
        pagos_id=[]
        for x in self.pago:
            pagos_id.append(x.id)
        
        pagos_id.append(pago_id)
        self.pago=pagos_id



class tipo_suscripcion(models.Model):
    _name = "gym.tipo_suscripcion"
    
    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    duracion = fields.Integer(string="Duración", required=True, default=1)
    unidad_duracion = fields.Selection(selection=[('dia', 'Día(s)'), ('semana', 'Semana(s)'), ('mes', 'mes(es)'),('ano','año(s)')], default='dia',required=True)
    costo = fields.Float(string="Costo", required=True)
    aplica_para = fields.Many2many('gym.tipo_miembro', string="Aplica para:")
    activo = fields.Boolean(string="Activo", default=True)
    
    
    
class tipo_pago(models.Model):
    _name = "gym.tipo_pago"
    
    name= fields.Char(string="Nombre",required=True)
    descripcion= fields.Text(string="Descripcion",required=True)
    

class pago(models.Model):
    _name ="gym.pago"
    miembro=fields.Many2one('gym.miembro')
    uid_transaccion=fields.Char()
    tipo_pago=fields.Many2one('gym.tipo_pago')
    cantidad=fields.Float()
    fecha=fields.Datetime()
    validado=fields.Boolean()



