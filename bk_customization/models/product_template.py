# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # BKB Boiler Manufacturing Specification Fields
    bkb_specification = fields.Char(
        string='SPECIFICATION',
        help='Product specification details'
    )
    
    bkb_model_no = fields.Char(
        string='MODEL NO.',
        help='Model number of the product'
    )
    
    bkb_size = fields.Char(
        string='SIZE',
        help='Size specifications'
    )
    
    bkb_sch = fields.Char(
        string='SCH.',
        help='Schedule information'
    )
    
    bkb_class = fields.Char(
        string='CLASS',
        help='Product class information'
    )
    
    bkb_long = fields.Char(
        string='LONG',
        help='Length specifications'
    )
    
    bkb_range = fields.Char(
        string='RANGE',
        help='Product range information'
    )
    
    bkb_ref_no = fields.Char(
        string='REF. NO.',
        help='Reference number'
    )
    
    bkb_make = fields.Char(
        string='MAKE',
        help='Manufacturer information'
    )
    
    bkb_press = fields.Char(
        string='PRESS.',
        help='Pressure specifications'
    )
    
    bkb_temp = fields.Char(
        string='TEMP.',
        help='Temperature specifications'
    )
    
    bkb_head = fields.Char(
        string='HEAD',
        help='Head specifications'
    )
    
    bkb_flow = fields.Char(
        string='FLOW',
        help='Flow specifications'
    )
    
    bkb_hp = fields.Char(
        string='HP',
        help='Horsepower specifications'
    )
    
    bkb_kw = fields.Char(
        string='KW',
        help='Kilowatt specifications'
    )
    
    bkb_rpm = fields.Char(
        string='RPM',
        help='Revolutions per minute specifications'
    )

    def _generate_bkb_description(self):
        """
        Generate description based on BKB specification fields.
        Returns a formatted string with non-empty specifications.
        """
        specs = []
        
        # Define field mappings with their display names
        field_mappings = [
            ('bkb_specification', 'SPECIFICATION'),
            ('bkb_model_no', 'MODEL NO.'),
            ('bkb_size', 'SIZE'),
            ('bkb_sch', 'SCH.'),
            ('bkb_class', 'CLASS'),
            ('bkb_long', 'LONG'),
            ('bkb_range', 'RANGE'),
            ('bkb_ref_no', 'REF. NO.'),
            ('bkb_make', 'MAKE'),
            ('bkb_press', 'PRESS.'),
            ('bkb_temp', 'TEMP.'),
            ('bkb_head', 'HEAD'),
            ('bkb_flow', 'FLOW'),
            ('bkb_hp', 'HP'),
            ('bkb_kw', 'KW'),
            ('bkb_rpm', 'RPM'),
        ]
        
        # Build specifications list
        for field_name, display_name in field_mappings:
            value = getattr(self, field_name, False)
            if value and value.strip():
                specs.append(f"{display_name}: {value.strip()}")
        
        return '\n'.join(specs) if specs else ''

    @api.model
    def create(self, vals):
        """
        Override create method to auto-populate description fields
        """
        # Call super to create the record
        record = super(ProductTemplate, self).create(vals)
        
        # Generate BKB description
        bkb_description = record._generate_bkb_description()
        
        # Update description fields if BKB description is generated
        if bkb_description:
            record.write({
                'description_purchase': bkb_description,
                'description_sale': bkb_description,
            })
        
        return record

    def write(self, vals):
        """
        Override write method to auto-populate description fields
        """
        # Call super to update the record
        result = super(ProductTemplate, self).write(vals)
        
        # Check if any BKB fields were updated
        bkb_fields = [
            'bkb_specification', 'bkb_model_no', 'bkb_size', 'bkb_sch',
            'bkb_class', 'bkb_long', 'bkb_range', 'bkb_ref_no', 'bkb_make',
            'bkb_press', 'bkb_temp', 'bkb_head', 'bkb_flow', 'bkb_hp',
            'bkb_kw', 'bkb_rpm'
        ]
        
        # Check if any BKB field was modified
        bkb_field_updated = any(field in vals for field in bkb_fields)
        
        if bkb_field_updated:
            # Generate new BKB description
            bkb_description = self._generate_bkb_description()
            
            # Update description fields
            update_vals = {}
            if bkb_description:
                update_vals.update({
                    'description_purchase': bkb_description,
                    'description_sale': bkb_description,
                })
            else:
                # If no BKB specs, clear the descriptions
                update_vals.update({
                    'description_purchase': '',
                    'description_sale': '',
                })
            
            # Write the updated descriptions
            if update_vals:
                super(ProductTemplate, self).write(update_vals)
        
        return result
