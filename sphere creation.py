import trimesh
import numpy as np
from py_lib3mf import Lib3MF

# Define sphere parameters
radius = 10
resolution = 0.5

# Create an icosphere mesh with trimesh
sphere = trimesh.creation.icosphere(radius=radius, subdivisions=int(1 / resolution))

# Create a material with a black color
black_material = trimesh.visual.material.SimpleMaterial(color=[0.0, 0.0, 0.0])

# Assign the material to the sphere mesh
sphere.visual.material = black_material

# Export the mesh to a 3MF file
output_file = "black_sphere.3mf"
with Lib3MF as lib3mf:
    model = lib3mf.create_model()
    mesh = model.add_mesh(sphere.vertices, sphere.faces)
    mesh.set_name("Black Sphere")
    mesh.set_material(black_material)
    model_writer = model.query_interface(Lib3MFModelWriter)
    model_writer.write_to_file(output_file)

print(f"Successfully created {output_file} with a black-colored sphere using 3MF format.")
