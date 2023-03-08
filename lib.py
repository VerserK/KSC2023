import flask
from flask import Flask ,session
from flask_cors import CORS, cross_origin
from flask import request
import psycopg2
from psycopg2 import Error
from typing import List, Tuple
import jsons
from flask import jsonify
from jsonify import convert
import uuid
import requests
import jwt
import json
import os