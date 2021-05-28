import csv
import os

from application import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




engine.execute('DROP TABLE IF EXISTS Users')

engine.execute('CREATE TABLE Users(id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, gender VARCHAR(5) NOT NULL, year integer NOT NULL, department VARCHAR(50) NOT NULL)')

engine.execute('CREATE TABLE Fkilo(id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, gender VARCHAR(5) NOT NULL, year integer NOT NULL, department VARCHAR(50) NOT NULL)')
engine.execute('CREATE TABLE Skilo(id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, gender VARCHAR(5) NOT NULL, year integer NOT NULL, department VARCHAR(50) NOT NULL)')
engine.execute('CREATE TABLE Fbekilo(id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, gender VARCHAR(5) NOT NULL, year integer NOT NULL, department VARCHAR(50) NOT NULL)')

# app = Flask(__name__)




