import streamlit as st
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdmolfiles
from stmol import showmol

# Function to convert SMILES to PDB
def smiles_to_pdb(smiles):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    pdb_str = rdmolfiles.MolToPDBBlock(mol)
    return pdb_str

# Function to convert SDF to PDB
def sdf_to_pdb(sdf):
    mol = Chem.MolFromMolBlock(sdf)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    pdb_str = rdmolfiles.MolToPDBBlock(mol)
    return pdb_str

# stmol function to render the molecule
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb, 'pdb')
    pdbview.setStyle({'stick': {}})  # Use 'stick' style for small molecules
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.spin(False)
    showmol(pdbview, height=500, width=800)

# Streamlit app
st.sidebar.title('SMILES/SDF to PDB Converter and 3D Viewer')
st.sidebar.write('Enter a SMILES string or upload an SDF file to convert it to a PDB file, view the result, and see a 3D visualization.')

# Option to choose input method
input_method = st.sidebar.radio("Choose input method:", ("SMILES", "SDF File"))

# SMILES input
if input_method == "SMILES":
    DEFAULT_SMILES = "CCO"
    txt = st.sidebar.text_area('Input SMILES', DEFAULT_SMILES, height=100)

# SDF file upload
elif input_method == "SDF File":
    sdf_file = st.sidebar.file_uploader("Upload SDF file", type=["sdf"])

# Update function to process the input and visualize the structure
def update():
    if input_method == "SMILES":
        smiles_input = txt
        if smiles_input:
            try:
                pdb_output = smiles_to_pdb(smiles_input)
                st.subheader("PDB Output")
                st.text_area("PDB", pdb_output, height=300)
                st.download_button("Download PDB File", pdb_output, file_name="output.pdb")
                
                st.subheader("3D Structure")
                render_mol(pdb_output)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning('👈 Enter a SMILES string!')

    elif input_method == "SDF File":
        if sdf_file is not None:
            sdf_content = sdf_file.read().decode("utf-8")
            try:
                pdb_output = sdf_to_pdb(sdf_content)
                st.subheader("PDB Output")
                st.text_area("PDB", pdb_output, height=300)
                st.download_button("Download PDB File", pdb_output, file_name="output.pdb")
                
                st.subheader("3D Structure")
                render_mol(pdb_output)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning('👈 Upload an SDF file!')

# Button to trigger the update function
predict = st.sidebar.button('Convert and Visualize', on_click=update)

# Warning if no input is provided
if not predict:
    st.warning('👈 Enter SMILES data or upload an SDF file and click the button!')

