import os
import sys

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class User_Recipes(db.model):
    __tablename__ = "user_recipes"

    user_id = db.column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_image = db.Column(db.String(2000), nullable=True)
    image_id = db.Column(db.Integer, db.ForeignKey("recipe_image.id"), nullable=False)
    description = db.Column(db.String(240), nullable=True)
    recipe_ingredients = db.Column(db.String, nullable=False)
    recipe_directions = db.Column(db.String, nullable=False)
    nutrition_facts_id = db.Column(db.Integer, db.ForeignKey("nutrition_facts.id"), nullable=False)

    def __repr__(self):
        return f'<User_Recipes {self.recipe_id}'
   
    def serialize(self):
        return {
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "recipe_title": self.recipe_title,
            "recipe_image": self.recipe_image,
            "description": self.description,
            "recipe_ingredients": self.recipe_ingredients,
            "recipe_directions": self.recipe_directions,
            "nutrition_facts_id": self.nutrition_facts_id
        }
    
# class Recipe_Image(db.model):
#     __tablename__ = "recipe_image"

#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
#     image_id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.Text, unique=True, nullable=True)
#     mimetype = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f'<Recipe_Image {self.image_id}'
    
#     def serialize(self):
#         return {
#             "user_id": self.user_id,
#             "image_id": self.image_id,
#             "image": self.image,
#             "name": self.name,
#             "mimetype": self.mimetype
#         }

class User_Categories(db.model):
    __tablename__ = "user_categories"

    user_id = db.column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(90), nullable=False)

    def __repr__(self):
        return f'<User_Categories {self.category_id}'
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "category_id": self.category_id,
            "category_name": self.category_name
        }

class Nutrition_Facts(db.model):
    __tablename__ = "nutrition_facts"

    user_id = db.column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    nutrition_facts_id = db.Column(db.Integer, primary_key=True)
    calories = db.Column(db.Float, nullable=False)
    protein_in_grams = db.Column(db.Float, nullable=False)
    carbohydrates_in_grams = db.Column(db.Float, nullable=False)
    fats_in_grams = db.Column(db.Float, nullable=False)
    sodium_in_mg = db.Column(db.Float, nullable=False)
    cholestorol_in_mg = db.Column(db.Float, nullable=False)
    fiber_in_grams = db.Column(db.Float, nullable=False)
    sugars_in_grams = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Nutrition_Facts {self.nutrition_facts_id}'
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "nutrition_facts_id": self.nutrition_facts_id,
            "calories": self.calories,
            "protein_in_grams": self.protein_in_grams,
            "carbohydrates_in_grams": self.carbohydrates_in_grams,
            "fats_in_grams": self.fats_in_grams,
            "sodium_in_mg": self.sodium_in_mg,
            "cholestorol_in_mg": self.cholestorol_in_mg,
            "fiber_in_grams": self.fiber_in_grams,
            "sugars_in_grams": self.sugars_in_grams
        }