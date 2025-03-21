"""
ROI Calculator Object
This module defines a class `ROI_Calc` that calculates the Return on Investment (ROI)
"""


class ROI_Calc:

    # Initialize the object with the final value of investment (FVI) and the cost of investment (CI)
    def __init__(self, fvi, ci):
        self.fvi = fvi
        self.ci = ci
        self.roi = 0.00

    def calc_roi(self):
        """
        Calculate the ROI based on the formula:
        ROI = (Net Profit / Cost of Investment) * 100
        ROI = ((FVI - CI) / CI) * 100
        """
        roi = round(((self.fvi - self.ci) / self.ci) * 100, 3)
        return roi

    def annual_roi(self, years):
        """
        Calculate the annualized ROI based on the formula(ROI must be a decimal value not a percentage):
        Annualized ROI = (((1 + (ROI))^(1/years)) - 1) * 100
        """
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")

        roi = self.calc_roi()
        annualized_roi = (((1 + (roi/100))**(1/years)) - 1) * 100
        annualized_roi = round(annualized_roi, 3)
        return annualized_roi