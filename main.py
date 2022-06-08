import bpy

bl_info = {
    "name": "SELECT MESH HELPER",
    "blender": (2, 80, 0),
    "category": "MY CUSTOM PLUGINS",
}

class PANEL1_PT_COMPAREHELPER(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "SelectHelper"
    bl_idname = "PANEL1_PT_COMPAREHELPER"
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_category    = "SelectHelper"
    bl_description = "My Compare Helper Plugin"

    def draw(self, context):
        lay = self.layout

        scene = context.scene
        
        try:
            lay.operator("op.select_narrow")
            lay.operator("op.select_wide")
            lay.separator()
            lay.operator("op.select_active")
            lay.operator("op.deselect_active")
            lay.separator()
            lay.operator("op.hide_selected")
            lay.operator("op.unhide_selected")
        except:
            print(failed)
        
    def execute(self, context):
         return {"FINISHED"}  
        


class SELECT_NARROW_OP(bpy.types.Operator):
    """Select Narrow Face Mesh"""
    bl_idname = "op.select_narrow"
    bl_label = "NARROW"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print('SELECT_NARROW_OP')
#        try:
#            bpy.ops.object.mode_set(mode='EDIT')
#        except:
#            print('MODE SWITCH FAILED')

        ## https://b3d.interplanety.org/en/how-to-set-object-mesh-to-active-in-blender-2-8-python-api/
        obj = context.window.scene.objects["MarkNarrow_FaceMesh_LOD0"]
        context.view_layer.objects.active = obj    # 'obj' is the active object now

        #bpy.ops.object.mode_set(mode = 'EDIT') 
        return {"FINISHED"}
    
class SELECT_WIDE_OP(bpy.types.Operator):
    """Select Wide Face Mesh"""
    bl_idname = "op.select_wide"
    bl_label = "WIDE"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print('SELECT_WIDE_OP')
        obj = context.window.scene.objects["MarkWide_FaceMesh_LOD0"]
        context.view_layer.objects.active = obj    # 'obj' is the active object now
        return {"FINISHED"}      
    
    
    
class SELECT_ACTIVE_OP(bpy.types.Operator):
    """SELECT_ACTIVE_OP"""
    bl_idname = "op.select_active"
    bl_label = "SELECT_ACTIVE"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.active_object.select_set(True)
        print('SELECT_ACTIVE__OP')
        return {"FINISHED"} 
        
class DESELECT_ACTIVE_OP(bpy.types.Operator):
    """DESELECT_ACTIVE_OP"""
    bl_idname = "op.deselect_active"
    bl_label = "DESELECT_ACTIVE"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.active_object.select_set(False)
        print('DESELECT_ACTIVE__OP')
        return {"FINISHED"} 
    
    
class HIDE_SELECTED_OP(bpy.types.Operator):  
    """HIDE_SELECTED_OP"""
    bl_idname = "op.hide_selected"
    bl_label = "HIDE ACTIVE"
    bl_options = {'REGISTER', 'UNDO'}  
    
    def execute(self, context):
        #bpy.context.active_object.hide_viewport = False
        #bpy.context.view_layer.active_layer_collection.hide_viewport = True
        bpy.context.object.hide_set(True)
        print('HIDE_SELECTED_OP')
        return {"FINISHED"}     
   
class UNHIDE_SELECTED_OP(bpy.types.Operator):  
    """UNHIDE_SELECTED_OP"""
    bl_idname = "op.unhide_selected"
    bl_label = "UNHIDE ACTIVE"
    bl_options = {'REGISTER', 'UNDO'}  
    
    def execute(self, context):
        #bpy.context.active_object.hide_viewport = False
        #bpy.context.view_layer.active_layer_collection.hide_viewport = True
        bpy.context.object.hide_set(False)
        print('UNHIDE_SELECTED_OP')
        return {"FINISHED"}      
    


def register():
    bpy.utils.register_class(PANEL1_PT_COMPAREHELPER)
    bpy.utils.register_class(SELECT_NARROW_OP)
    bpy.utils.register_class(SELECT_WIDE_OP)
    bpy.utils.register_class(SELECT_ACTIVE_OP)
    bpy.utils.register_class(DESELECT_ACTIVE_OP)
    bpy.utils.register_class(HIDE_SELECTED_OP)
    bpy.utils.register_class(UNHIDE_SELECTED_OP)


def unregister():
    bpy.utils.register_class(PANEL1_PT_COMPAREHELPER)
    bpy.utils.register_class(SELECT_NARROW_OP)
    bpy.utils.register_class(SELECT_WIDE_OP)
    bpy.utils.register_class(SELECT_ACTIVE_OP)
    bpy.utils.register_class(DESELECT_ACTIVE_OP)
    bpy.utils.register_class(HIDE_SELECTED_OP)
    bpy.utils.register_class(UNHIDE_SELECTED_OP)

if __name__ == "__main__":
    register()
