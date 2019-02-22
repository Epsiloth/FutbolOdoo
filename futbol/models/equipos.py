from odoo import models, fields, api

class Equipos(models.Model):
    _name = 'futbol.equipos'
    nombre = fields.Char('Nombre', required=True)
    pais = fields.Many2one('futbol.paises', 'País', required=True)
    entrenador = fields.Many2one('futbol.entrenadores', 'Entrenador', required=True, domain="[('pais', '=', 'pais')]")
    jugador1 = fields.Many2one('futbol.jugadores', 'Jugador 1', required=True, domain=[('pais', '=', 'pais')])
    jugador2 = fields.Many2one('futbol.jugadores', 'Jugador 2', required=True, domain=[('pais', '=', 'pais')])
    jugador3 = fields.Many2one('futbol.jugadores', 'Jugador 3', required=True, domain=[('pais', '=', 'pais')])
    jugador4 = fields.Many2one('futbol.jugadores', 'Jugador 4', required=True, domain=[('pais', '=', 'pais')])
    jugador5 = fields.Many2one('futbol.jugadores', 'Jugador 5', required=True, domain=[('pais', '=', 'pais')])

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
