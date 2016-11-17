# -*- coding: utf-8 -*-
from openerp import fields, models, api, _


class WebsiteStaticTemplate(models.Model):
    _name = 'website.static.template'

    name = fields.Char(string='Name', required=True, help='Name of the template.')
    active = fields.Boolean(default=True)
    blocks_id = fields.One2many('website.static', 'template_id', string="Template Blocks")


class WebsiteStatic(models.Model):
    _name = 'website.static'
    _rec_name = 'file_name'

    template_id = fields.Many2one('website.static.template', string='Static Template', required=True)
    file_name = fields.Char(string='File Name', required=True, help='Name of the file.')
    block_name = fields.Char(string='Block Name', required=True, help='Block name of the file.')
    original_block = fields.Text(string='Original Block', help='Original block of the template e.g. lorem ipsum ..')
    template_block = fields.Text(string='Template Block', help='Block of the template.')
