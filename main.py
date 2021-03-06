import kivy.app
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.widget import Widget
import Fruits
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import math



class FirstApp(kivy.app.App):


    def classify_image11(self):

        img_path = self.root.ids["img11"].source

        img_features = Fruits.extract_features(img_path)

        predicted_class11 = Fruits.predict_output("weighttss.npy", img_features, activation="sigmoid")

        self.root.ids["label11"].text = "Predicted Class : " + predicted_class11

        if str(predicted_class11) == "jjampong":
            self.root.ids["_calorie1"].text = '764'
        elif str(predicted_class11) == "salad":
            self.root.ids["_calorie1"].text = '201'
        elif str(predicted_class11) == "toast":
            self.root.ids["_calorie1"].text = '420'
        else:
            self.root.ids["_calorie1"].text = '128'


    def classify_image22(self):
        img_path = self.root.ids["img22"].source

        img_features = Fruits.extract_features(img_path)

        predicted_class22 = Fruits.predict_output("weighttss.npy", img_features, activation="sigmoid")

        self.root.ids["label22"].text = "Predicted Class : " + predicted_class22

        if str(predicted_class22) == "jjampong":
            self.root.ids["_calorie2"].text = '764'
        elif str(predicted_class22) == "salad":
            self.root.ids["_calorie2"].text = '201'
        elif str(predicted_class22) == "toast":
            self.root.ids["_calorie2"].text = '420'
        else:
            self.root.ids["_calorie2"].text = '128'

    def classify_image33(self):
        img_path = self.root.ids["img33"].source

        img_features = Fruits.extract_features(img_path)

        predicted_class33 = Fruits.predict_output("weighttss.npy", img_features, activation="sigmoid")

        self.root.ids["label33"].text = "Predicted Class : " + predicted_class33

        if str(predicted_class33) == "jjampong":
            self.root.ids["_calorie3"].text = '764'
        elif str(predicted_class33) == "salad":
            self.root.ids["_calorie3"].text = '201'
        elif str(predicted_class33) == "toast":
            self.root.ids["_calorie3"].text = '420'
        else:
            self.root.ids["_calorie3"].text = '128'


    def image_select(self, filename):
        self.root.ids.img11.source = filename[0]

    def image_select1(self, filename):
        self.root.ids.img22.source = filename[0]

    def image_select2(self, filename):
        self.root.ids.img33.source = filename[0]

    def speed_calc(self, _a, hard111):
        self.root.ids["_speed1"].text = str( float(152.35) * math.log10(14-(float(0.008865) * float(hard111.text) / float(_a.text) / float(30))) + 252.38)


class LoadDialog:
    pass


if __name__ == "__main__":

    firstApp = FirstApp(title="Fruits 360 Recognition.")
    firstApp.run()

