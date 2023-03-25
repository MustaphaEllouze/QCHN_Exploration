class ExplorationSave :
    
    save = []

    def log_action(
            name_function:str,
            arguments:tuple,
    ):
        ExplorationSave.save.append((name_function,arguments))
    
    def write_save(
        path_fichier:str
    ):
        with open(f'{path_fichier}.save','w') as f:
            for action in ExplorationSave.save :
                f.write(
                    f'{action[0]}'
                )
                for arg in action[1]:
                    f.write(
                        f' {arg}'
                    )
                f.write('\n')
    