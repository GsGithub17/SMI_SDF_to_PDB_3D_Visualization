# SMILES/SDF to PDB Converter and 3D Viewer

This Streamlit application allows users to convert SMILES strings or SDF files to PDB format and visualize the 3D structure of the molecules. The application uses RDKit for conversion and py3Dmol for visualization.

## Features

- Convert SMILES strings to PDB format
- Convert SDF files to PDB format
- Visualize the 3D structure of the molecule using py3Dmol
- Download the PDB file

## Installation

To run this application, you need to have Python installed. You can install the required packages using pip:

```bash
pip install streamlit rdkit py3Dmol stmol
```

## Usage

1. Clone this repository or download the visualize_pdb.py script.
2. Navigate to the directory containing the visualize_pdb.py script.
3. Run the Streamlit app:

```bash
streamlit run sdf_smiles_to_pdb3D.py
```

## How to Use

1. Choose Input Method: Select either "SMILES" or "SDF File" from the sidebar.
2. SMILES Input:
   Enter a SMILES string in the text area provided.
3. Click the "Convert and Visualize" button.
   SDF File Upload:
   Upload an SDF file using the file uploader.
   Click the "Convert and Visualize" button.
4. View Results:
   The PDB format of the molecule will be displayed in a text area.
   A download button will be provided to download the PDB file.
   The 3D structure of the molecule will be visualized below.
## Example

Input SMILES: Enter CCO (ethanol) in the SMILES input area.
Upload SDF File: Upload an SDF file containing the molecule information.
Visualize: Click on "Convert and Visualize" to see the PDB output and 3D structure.

## Dependencies

Streamlit: An app framework for Machine Learning and Data Science.
RDKit: A collection of cheminformatics and machine learning tools.
py3Dmol: A Python wrapper for 3Dmol.js to visualize molecular data.
stmol: Streamlit component to integrate py3Dmol visualizations.

## License

This project is licensed under the MIT License.

## Acknowledgments

Inspired by the Streamlit and RDKit communities.
Special thanks to the developers of py3Dmol and stmol for their amazing tools.




# SMI_SDF_to_PDB_3D_Visualization
