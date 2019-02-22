from odoo import models, fields, api

class Entrenadores(models.Model):
    _name = 'futbol.entrenadores'
    foto = fields.Binary('Foto', required=False)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    pais = fields.Many2one('futbol.paises', 'País', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res