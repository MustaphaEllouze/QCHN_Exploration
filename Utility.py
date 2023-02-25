class EDateTime : 
    """Représente l'heure et la date du jeu
    """
    def __init__(
            self,
            heure_depart=8.0,
            jour_depart=1,
    ):
        assert heure_depart<24.0
        assert jour_depart>=1.0

        self.day = int(jour_depart)
        self.hour = int(heure_depart)
        self.minutes=int((heure_depart-self.hour)*60)
    
    def pass_hours(
            self,
            hours=0,
    ):
        """Avance de 'hours' heures

        Args:
            hours (int, optional): Hours to pass. Defaults to 0.
        """
        days_to_pass = hours//24
        hours_to_pass = hours%24

        self.day += days_to_pass
        self.hour += int(hours_to_pass)
        
        self.minutes += int((hours-int(hours))*60)

        if(self.minutes>=60.0): 
            self.minutes -= 60.0
            self.hour += 1       
        
        if(self.hour>=24.0): 
            self.hour -= 24.0
            self.day += 1
    
    def pass_minutes(
            self,
            minutes=0,
    ):
        """Avance de 'minutes' minutes

        Args:
            minutes (int, optional): Minutes to pass. Defaults to 0.
        """
        self.pass_hours(minutes/60)
    
    def __str__(self):
        return f'Jour {int(self.day)} : {str(int(self.hour)).zfill(2)}h{str(int(self.minutes)).zfill(2)}'


if __name__ == '__main__':
    test = EDateTime(heure_depart=8,jour_depart=1)
    print(test)
    test.pass_hours(2.5)
    print(test)
    test.pass_minutes(42.5)
    print(test)
    test.pass_minutes(1234.5)
    print(test)