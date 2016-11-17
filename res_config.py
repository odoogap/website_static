# -*- encoding: utf-8 -*-
import os
from openerp import fields, models, api, _
from openerp.exceptions import ValidationError
from lxml import etree

WWW__ROOT = os.path.join(os.path.dirname(__file__), 'www')


class website_config_settings(models.TransientModel):
    _inherit = 'website.config.settings'

    @api.multi
    def execute_getattributes(self):
        if not self.template_name:
            raise ValidationError(_('You must first chose an empty template.'))
        if len(self.template_name.blocks_id)>0:
            raise ValidationError(_('This template is not empty.'))
        tpl_id = self.template_name.id
        for subdir, dirs, files in os.walk(WWW__ROOT):
            for file in files:
                print os.path.join(subdir, file)
                extension = os.path.splitext(file)[1]
                if extension == '.html':
                    doc = etree.parse(os.path.join(subdir, file))
                    for node in doc.xpath("//*[@doo]"):
                        print node.text, node.attrib['doo'], file
                        self.env['website.static'].sudo().create({
                            'template_id': tpl_id,
                            'file_name': file,
                            'block_name': node.attrib['doo'],
                            'original_block': node.text,
                            'template_block': node.text,
                        })
    @api.multi
    def execute_publish(self):
        for subdir, dirs, files in os.walk(WWW__ROOT):
            for file in files:
                print os.path.join(subdir, file)
                extension = os.path.splitext(file)[1]
                if extension == '.html':
                    doc = etree.parse(os.path.join(subdir, file))

                    for node in doc.xpath("//*[@doo]"):
                        if node.attrib['doo'] == 'text':
                            print node.text
                    #doc.write(os.path.join(subdir, file), pretty_print=True)

    @api.model
    def _default_template(self):
        try:
            tpl_id = int(self.env['ir.config_parameter'].sudo().get_param('website_static.template_name_id'))
            if tpl_id:
                return tpl_id
        except:
            return False

    template_name = fields.Many2one('website.static.template', string='Static Template', default=_default_template)

    @api.multi
    def set_template_name(self):
        for rec in self:
            if rec.template_name:
                self.env['ir.config_parameter'].sudo().set_param('website_static.template_name_id', rec.template_name.id)
            else:
                self.env['ir.config_parameter'].sudo().set_param('website_static.template_name_id', '')
