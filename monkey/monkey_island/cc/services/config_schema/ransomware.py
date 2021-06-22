RANSOMWARE = {
    "title": "Ransomware",
    "type": "object",
    "properties": {
        "directories": {
            "title": "Directories to encrypt",
            "type": "object",
            "properties": {
                "linux_dir_ransom": {
                    "title": "Linux encryptable directory",
                    "type": "string",
                    "default": "",
                    "description": "Files in the specified directory will be encrypted "
                    "using bitflip to simulate ransomware.",
                },
                "windows_dir_ransom": {
                    "title": "Windows encryptable directory",
                    "type": "string",
                    "default": "",
                    "description": "Files in the specified directory will be encrypted "
                    "using bitflip to simulate ransomware.",
                },
            },
        }
    },
}
