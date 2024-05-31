import bpy
from mathutils import Vector
import sys
import bmesh

#Obtener la ruta del archivo .stl desde los argumentos de la línea de comandos
argv = sys.argv
output_path = "c:/Users/carbe/OneDrive/Documents/Blender/Prueba1.blend"



def extrusion(x):
    m = (float(x))*-1
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(-0, -0, m), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.transform.resize(value=(1, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)

def calculate_volume(obj):
    # Asegurarnos de que estamos en "Object" mode
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    # Aplicar transformacion para asegurar un buen calculo de volumen
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    # Cambiar a edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(obj.data)
    # Calcular volumen de Bmesh
    volume = bm.calc_volume(signed=True)
    # Regresar a object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    return volume

#Obtener solo los argumentos después de "--"
if "--" in argv:
    argv = argv[argv.index("--") + 1:]

if not argv:
    print("hola")
    raise ValueError("No se proporcionó la ruta del archivo .stl")
    
funcion = argv[0]
if funcion == "importar":

    archivo_stl = argv[1]  # La ruta del archivo .stl es el primer argumento

    #Borra lo que aparece al inicio
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    #Importar el archivo STL
    bpy.ops.import_mesh.stl(filepath=archivo_stl)

    # Obtener el objeto importado (asume que es el único objeto en la escena)
    obj = bpy.context.selected_objects[0]

    #Selecciona el stl
    bpy.ops.object.select_all(action='SELECT')
    #Aplica modificador "Solidify" para hacer el objeto un solido.
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    bpy.ops.object.modifier_apply(modifier="Solidify")

    # Ruta donde deseas guardar el archivo .blend
    output_path = "c:/Users/carbe/OneDrive/Documents/Blender/Prueba1.blend"


    # Guardar el archivo .blend sin aplicar transformaciones
    bpy.ops.wm.save_as_mainfile(filepath=output_path, check_existing=False)
    
elif funcion == "extrusion":
    metros = str(argv[1])
    #Ruta donde se guardo el archivo
    archivo_blend = output_path
    #abrir archivo
    bpy.ops.wm.open_mainfile(filepath=archivo_blend)
    # Define the threshold for considering a face as facing downward
    downward_threshold = -0.5  # A value close to -1 indicates a stricter downward orientation
    altura_maxima_z = 4
    bpy.ops.object.select_all(action='SELECT')
    # Get the active object
    obj = bpy.context.object

    # Ensure we are in edit mode and switch to it if necessary
    if obj.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')

    # Create a BMesh representation of the object
    bm = bmesh.from_edit_mesh(obj.data)

    # Ensure we are selecting faces
    bpy.ops.mesh.select_mode(type="FACE")

    # Deselect all faces
    bpy.ops.mesh.select_all(action='DESELECT')

    # Select faces based on their normal direction
    for face in bm.faces:
        # Obtener el centro de la cara en coordenadas globales
        face_center = obj.matrix_world @ face.calc_center_median()
        # Check if the face normal is pointing downwards
        if face.normal.z < downward_threshold:
            if face_center.z < altura_maxima_z:
                face.select = True

    # Update the mesh with the changes
    bmesh.update_edit_mesh(obj.data)
    extrusion(metros)
    
        # Get the active object
    obj = bpy.context.object

    if obj is not None and obj.type == 'MESH':
        volume = calculate_volume(obj)
        print(f"Volume of the object: {volume} cubic units")
    else:
        print("Please select a mesh object.")


    # Ruta donde deseas guardar el archivo .blend
    output_path = "c:/Users/carbe/OneDrive/Documents/Blender/Prueba1.blend"


    # Guardar el archivo .blend sin aplicar transformaciones
    bpy.ops.wm.save_as_mainfile(filepath=output_path, check_existing=False)

elif funcion == "ver":
    #Ruta donde se guardo el archivo
    archivo_blend = output_path
    #abrir archivo
    bpy.ops.wm.open_mainfile(filepath=archivo_blend)
    
    
elif funcion == "guardar":
     # Guardar el archivo .blend sin aplicar transformaciones
    bpy.ops.wm.save_as_mainfile(filepath=output_path, check_existing=False)