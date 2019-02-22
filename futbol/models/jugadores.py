from odoo import models, fields, api

class Jugadores(models.Model):
    _name = 'futbol.jugadores'
    foto = fields.Binary('Foto', required=False)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellido', required=True)
    pais = fields.Many2one('futbol.paises', 'País', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res