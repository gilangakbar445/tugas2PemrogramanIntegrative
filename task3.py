class BMI:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height
    
    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    def BMI_Value(self):
        bmi = self._weight / (self._height ** 2)
        return bmi

inputWeight = input("masukkan berat badan (dalam Kg) : ")
inputHeight = input("masukkan tinggi badan (dalam Meter) : ")

bmi = BMI(weight=int(inputWeight),height=int(inputHeight))
print("Weight:", bmi.weight, "kg")
print("Height:", bmi.height, "m")
bmiValue = bmi.BMI_Value()
print(f"BMI Value : {bmiValue}")