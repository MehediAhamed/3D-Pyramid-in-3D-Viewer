import bpy
import math

#clear the existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

#Create a new mesh and an object to link it with 
mesh=bpy.data.meshes.new(name="Pyramid")
obj=bpy.data.objects.new("Pyramid",mesh)

#Link object to the scene
scene=bpy.context.scene
scene.collection.objects.link(obj)

# Define the vertices and faces of the pyramid
vertices = [
    (1, 1, 0),  # Bottom left
    (1, -1, 0),  # Bottom right
    (-1, -1, 0),  # Top right
    (-1, 1, 0),  # Top left
    (0, 0, math.sqrt(2))  # Apex
]

faces = [
    (0, 1, 4),  # Bottom face
    (1, 2, 4),  # Right face
    (2, 3, 4),  # Top face
    (3, 0, 4),  # Left face
    (3, 0, 1, 2)  # Base face
]

# Update the mesh with pyramid data
mesh.from_pydata(vertices, [], faces)
mesh.update()


# Center the pyramid in the scene.
obj.location.x = 0
obj.location.y = 0
obj.location.z = 0

# Export the pyramid model in GLTF format.
bpy.ops.export_scene.gltf(filepath="../../three.js/models/pyramid.gltf")