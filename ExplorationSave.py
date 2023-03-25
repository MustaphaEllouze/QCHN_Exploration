class ExplorationSave :
    
    save = []
    write_mode = True

    def log_action(
            name_function:str,
            arguments:tuple,
            force:bool=False,
    ):
        if ExplorationSave.write_mode or force : ExplorationSave.save.append((name_function,arguments))
    
    def already_logged(
            string:str,
            force:bool=False,
    ):
        fonction = string.split('|')[0].strip()
        arguments = string.strip().split('|')[1].split()
        ExplorationSave.log_action(fonction,tuple(arguments),force=force)
    
    def write_save(
        path_fichier:str
    ):
        with open(f'{path_fichier}.save','w') as f:
            for action in ExplorationSave.save :
                f.write(
                    f'{action[0]} |'
                )
                for arg in action[1]:
                    f.write(
                        f' {arg}'
                    )
                f.write('\n')
    