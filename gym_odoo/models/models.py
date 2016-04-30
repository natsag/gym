# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class gym(models.Model):
#     _name = 'gym.gym'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class miembro(models.Model):
	_name = 'gym.miembro'

	name = fields.Char(string="Nombre", required=True)
	telefono = fields.Char(string="Teléfono",required=True)
	email = fields.Char(string="Email",required=True)
	direccion = fields.Text(string="Dirección",required=True)
	facturar = fields.Boolean(String="¿Requiere factura?")
	datos_facturacion = fields.Many2one('gym.datos_facturacion', required=True)

class datos_facturacion(models.Model):
	_name = 'gym.datos_facturacion'

	name = fields.Char(string="Nombre o Razón social", required=True)
	RFC = fields.Char(required=True)
	telefono = fields.Char(required=True)
	email = fields.Char(required=True)
	direccion = fields.Text(required=True)

class suscripcion(models.Model):
	_name = "gym.suscripcion"
	
	miembro = fields.Many2one('gym.miembro', required=True,ondelete='cascade')
	tipo = fields.Many2one('gym.tipo_suscripcion', required=True,ondelete='cascade')
	inicio =fields.Date(string="Fecha de inicio",required=True)

class tipo_suscripcion(models.Model):
	_name="gym.tipo_suscripcion"
	
	name=fields.Char(string="Nombre",required=True)
	costo=fields.Float(string="Costo",required=True)
	
	

