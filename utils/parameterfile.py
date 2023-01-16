### Import standard modules
import json

### Import external modules
import yaml

### Import personal modules
from console import Console
from filename import FileName
   
### Retrieve Json or Yaml Content
class ParameterFile():
    def __init__(self, filename="", colored=True):
        self.filename = FileName()
        self.parameters={}
        self.console = Console(colored)         # TODO: Review class ParameterFile to use logger instead of console
        if filename:
            self.filename = FileName(filename)
            self.load()
        
    def load(self):
        """Return a Dictionnary from Json or Yaml file

        Args:
            filename (file): File Name containing settings. Supported format : Json or Yaml

        Returns:
            Dictionnary: [A Dictionnary build from Json/YAML]
        """
        self.parameters = {}
        filetype = self.filename.fileextension.lower()

        supported_filetype = [".json", ".yaml", ".yml"]
        if filetype not in supported_filetype:
            self.console.print_msg("ERROR",f"Parameter file supports following format only: json, yml, yaml.")
        else:
            try:
                if filetype == ".json":
                    with open(self.filename.fullpath) as config_file:
                        self.parameters = json.load(config_file)
                elif filetype == ".yaml" or filetype == ".yml" :
                    with open(self.filename.fullpath) as config_file:
                        self.parameters = yaml.safe_load(config_file)
            except Exception as e:
                self.console.print_msg("ERROR",f"with Parameter File '{self.filename.fullpath}':")
                self.console.print_msg("ERROR",f"{str(e)}")
            else:
                self.console.print_msg("SUCCESS",f"Parameter file '{self.filename.fullpath}' successfuly loaded")

        return self.parameters

if __name__ == "__main__":
    import os
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    paramfile = os.path.join(CUR_DIR,"../data/sample.yaml")
    param_object =ParameterFile(paramfile)
    print(param_object.parameters)