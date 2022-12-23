def press_it(self, pressed):
    if pressed == "C":
        self.outputLabel.setText("0")
    else:
        self.outputLabel.setText(f'{self.outputLabel.text()} {pressed}')
