"""Custom file to read configs/files"""
import json
import os

import yaml

from bidgely.definitions import CONFIGS_FOLDER


class ConfigUtils:
    """Class to load configs as per system type"""

    def read_file(self, path):
        """
        Reads the yaml/text file and returns the content in yaml/json format
        :param environment:
        :param path:
        :return:
        """
        parent_path = self.get_parent_directory()
        if os.path.join(path).endswith('.yaml'):
            with open(parent_path + path) as f:
                configs = yaml.load(f, Loader=yaml.FullLoader)
                return configs
        elif os.path.join(path).endswith('.txt') or os.path.join(path).endswith('.json'):
            try:
                with open(parent_path + path) as f:
                    expected_data = json.load(f)
            except Exception:
                with open(path) as f:
                    expected_data = json.load(f)

        return expected_data

    @staticmethod
    def get_parent_directory():
        """
        returns the config file path
        :return:
        """
        return CONFIGS_FOLDER
