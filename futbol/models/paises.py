from odoo import models, fields, api

class Paises(models.Model):
    _name = 'futbol.paises'
    bandera = fields.Binary('Bandera', required=True)
    nombre = fields.Char('Nombre', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res