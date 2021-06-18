from odoo import api, fields, models


class Project(models.Model):
    _name = 'construction.project'
    _description = 'Proyectos de obras'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')

    cost = fields.Float(digits=(6,4), string='Costo', compute='_get_cost_stage', store=True)
    unit = fields.Many2one( 'construction.unit', string='Unidad', ondelete='set null', index=True, copy=False)

    stages = fields.One2many('construction.stage','project_id', string='Partida')

    forge_model_name = fields.Char(string='Nombre del modelo')
    forge_model_id = fields.Char(string='Id del modelo' )
    forge_model_select = fields.Char(string='Seleccionar modelo')
    # bc3_file = fields.Binary('Importar archivo bc3')
    # print(bc3_file)

    @api.depends('stages')
    def _get_cost_stage(self):
        for rec in self:
            total = 0
            for row in rec.stages:
                total += row.cost
            rec['cost'] = total
        
    # def import_bc3_file(self):
    #     for rec in self:
    #         print('excel')
    #         print(rec.bc3_file)
        # if '.xlsx' in list_file_name[int(tokens[2])].lower():
        #         xlsxPath = cwd+'/'+list_file_name[int(tokens[2])]
        #         xlsxFile = pd.read_excel(xlsxPath)
        #         print(xlsxFile)

class Stage(models.Model):
    _name = 'construction.stage'
    _description = 'Partidas de un proyecto'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    cost = fields.Float(digits=(6,4), string='Costo', compute='_get_cost_stage', store=True)
    unit = fields.Many2one( 'construction.unit', string='Unidad', ondelete='set null', index=True, copy=False)

    project_id = fields.Many2one('construction.project', string='Obra/Proyecto',  ondelete='cascade', index=True, copy=False)
    project_forge_model_name = fields.Char( related="project_id.forge_model_name", string="Nombre del modelo")
    project_forge_model_id = fields.Char( related="project_id.forge_model_id", string="Id del modelo")

    concepts = fields.One2many('construction.stage_concept_lines','stage_id', string='Concepto')

    bim_model_viewer = fields.Char(string="Visualizar modelo BIM")
    
    @api.depends('concepts')
    def _get_cost_stage(self):
        for rec in self:
            total = 0
            for row in rec.concepts:
                total += row.s_import
            rec['cost'] = total

class Stage_concept_lines(models.Model):
    _name = 'construction.stage_concept_lines'
    _description = 'partida concepto'

    quantity = fields.Float( string='Cantidad', default='1' )
    s_import = fields.Float( digits=(6,4), string='Importe', compute='_get_subtotal', store=True)

    stage_id = fields.Many2one('construction.stage', string='Partida',  ondelete='cascade', index=True, copy=False)
    concept_id = fields.Many2one('construction.concept', string='Concepto',  ondelete='cascade', index=True, copy=False)
    concept_cost = fields.Float( related='concept_id.cost', string='Costo')
    concept_unit = fields.Many2one( related='concept_id.unit', string='Unidad')

    @api.depends('quantity','concept_cost')
    def _get_subtotal(self):
        for rec in self:
            rec['s_import'] = rec.quantity * rec.concept_cost

class Concept(models.Model):
    _name = 'construction.concept'
    _description = 'Conceptos'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    description = fields.Html(string='Descripción')
    unit = fields.Many2one( 'construction.unit', string='Unidad', ondelete='set null', index=True, copy=False)

    cost = fields.Float(digits=(6,4), string='Costo', compute='_get_cost_concept', store=True)
    material_import = fields.Float(digits=(6,2), string='importe de materiales', compute='_get_material_import', store=True)
    workforce_import = fields.Float(digits=(6,2), string='importe de mano de obra', compute='_get_workforce_import', store=True)
    machinery_import = fields.Float(digits=(6,2), string='importe de maquinaria', compute='_get_machinery_import', store=True)
    basic_import = fields.Float(digits=(6,2), string='importe de básicos', compute='_get_basic_import', store=True)

    stage_id = fields.Many2one('construction.stage', string='Partida',  ondelete='cascade', index=True, copy=False)
    concept_material_lines = fields.One2many('construction.concept_material_lines','concept_id', string='Concepto')
    concept_workforce_lines = fields.One2many('construction.concept_workforce_lines','concept_id', string='Concepto')
    concept_machinery_lines = fields.One2many('construction.concept_machinery_lines','concept_id', string='Concepto')
    concept_basic_lines = fields.One2many('construction.concept_basic_lines','concept_id', string='Concepto')

    @api.depends('material_import','workforce_import','machinery_import','basic_import')
    def _get_cost_concept(self):
        for rec in self:
            rec['cost'] = rec.material_import + rec.workforce_import + rec.machinery_import + rec.basic_import

    @api.depends('concept_material_lines')
    def _get_material_import(self):
        for rec in self:
            total = 0
            for row in rec.concept_material_lines:
                total += row.m_import
            rec['material_import'] = total

    @api.depends('concept_workforce_lines')
    def _get_workforce_import(self):
        for rec in self:
            total = 0
            for row in rec.concept_workforce_lines:
                total += row.w_import
            rec['workforce_import'] = total

    @api.depends('concept_machinery_lines')
    def _get_machinery_import(self):
        for rec in self:
            total = 0
            for row in rec.concept_machinery_lines:
                total += row.m_import
            rec['machinery_import'] = total

    @api.depends('concept_basic_lines')
    def _get_basic_import(self):
        for rec in self:
            total = 0
            for row in rec.concept_basic_lines:
                total += row.b_import
            rec['basic_import'] = total


class Concept_basic_lines(models.Model):
    _name = 'construction.concept_basic_lines'
    _description = 'concepto básicos'

    quantity = fields.Float( string='Cantidad', default='1' )
    b_import = fields.Float( digits=(6,4), string='Importe', compute='_get_subtotal', store=True)

    concept_id = fields.Many2one('construction.concept', string='Concepto',  ondelete='cascade', index=True, copy=False)
    basic_id = fields.Many2one('construction.basic', string='Básico',  ondelete='cascade', index=True, copy=False)
    basic_cost = fields.Float( related='basic_id.cost', string='Costo', store=True)
    basic_unit = fields.Many2one( related='basic_id.unit', string='Unidad')

    @api.depends('quantity','basic_cost')
    def _get_subtotal(self):
        for rec in self:
            rec['b_import'] = rec.quantity * rec.basic_cost

class Basic(models.Model):
    _name = 'construction.basic'
    _description = 'Básicos'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    description = fields.Html(string='Descripción')
    unit = fields.Many2one( 'construction.unit', string='Unidad', ondelete='set null', index=True, copy=False)

    cost = fields.Float(digits=(6,4), string='Costo', compute='_get_cost_concept', store=True)
    material_import = fields.Float(digits=(6,2), string='importe de materiales', compute='_get_material_import', store=True)
    workforce_import = fields.Float(digits=(6,2), string='importe de mano de obra', compute='_get_workforce_import', store=True)
    machinery_import = fields.Float(digits=(6,2), string='importe de maquinaria', compute='_get_machinery_import', store=True)

    basic_material_lines = fields.One2many('construction.basic_material_lines','basic_id', string='básico')
    basic_workforce_lines = fields.One2many('construction.basic_workforce_lines','basic_id', string='básico')
    basic_machinery_lines = fields.One2many('construction.basic_machinery_lines','basic_id', string='básico')

    @api.depends('material_import','workforce_import','machinery_import')
    def _get_cost_concept(self):
        for rec in self:
            rec['cost'] = rec.material_import + rec.workforce_import + rec.machinery_import

    @api.depends('basic_material_lines')
    def _get_material_import(self):
        for rec in self:
            total = 0
            for row in rec.basic_material_lines:
                total += row.m_import
            rec['material_import'] = total

    @api.depends('basic_workforce_lines')
    def _get_workforce_import(self):
        for rec in self:
            total = 0
            for row in rec.basic_workforce_lines:
                total += row.w_import
            rec['workforce_import'] = total

    @api.depends('basic_machinery_lines')
    def _get_machinery_import(self):
        for rec in self:
            total = 0
            for row in rec.basic_machinery_lines:
                total += row.m_import
            rec['machinery_import'] = total