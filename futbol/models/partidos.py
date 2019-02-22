from odoo import models, fields, api

class Partidos(models.Model):
    _name = 'futbol.partidos'
    fecha = fields.Date('Fecha', required=True)
    pais = fields.Many2one('futbol.paises', 'País', required=True)
    anfitrion = fields.Many2one('futbol.equipos', 'Equipo Anfitrión', required=True, domain=[('pais', '=', 'pais')])
    resultAnfitrion = fields.Integer('Resultado Anfitrión', required=True)
    visitante = fields.Many2one('futbol.equipos', 'Equipo Visitante', required=True)
    resultVisitante = fields.Integer('Resultado Visitante', required=True)