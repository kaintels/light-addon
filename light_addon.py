import bpy
import random


def generate(context, min, max, amounts):
    for i in range(0, amounts):
        x = random.uniform(min, max)
        y = random.uniform(min, max)
        z = random.uniform(0, abs(max))
        
        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(x, y, z), scale=(1, 1, 1))


class LightGenOperator(bpy.types.Operator):
    bl_label = "Generate!"
    bl_idname = "object.lightgen_operator"
    def execute(self, context):
        generate(context, -context.scene.min_number, context.scene.max_number, context.scene.amount)
        return {'FINISHED'}

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Random Light Setting"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        # Create a simple row.
        layout.label(text="Light number")

        row = layout.row()
        row.prop(scene, "min_number")
        row.prop(scene, "max_number")
        
        layout.label(text="Amounts")
        row = layout.row()
        row.prop(scene, "amount")

        layout.label(text="Generation")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.lightgen_operator")

def register():
    bpy.types.Scene.min_number = bpy.props.IntProperty(name="Min number", default=1)
    bpy.types.Scene.max_number = bpy.props.IntProperty(name="Max number", default=1)
    bpy.types.Scene.amount = bpy.props.IntProperty(name="Amount", default=1)
    bpy.utils.register_class(LightGenOperator)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    del bpy.types.Scene.min_number
    del bpy.types.Scene.max_number
    del bpy.types.Scene.amount
    bpy.utils.unregister_class(LightGenOperator)
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
