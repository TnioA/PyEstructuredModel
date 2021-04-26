from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, current_app, jsonify
from App.Repository.AddressRepository import AddressRepository
from App.Controller.BaseController import BaseController
from App.Model.AddressModel import AddressModel
addressController = Blueprint('address', __name__, url_prefix='/address')

class AddressController(BaseController):
    def __init__(self):
        self.repository = AddressRepository()

    @addressController.route('/getbyzipcode', methods=['GET'])
    def GetByZipCode():
        zipCode = "60347152"
        repository = AddressRepository()
        response = repository.GetAddress(zipCode)
        address = AddressModel(response["cep"], response["logradouro"], response["complemento"], response["localidade"], response["uf"])
        
        return jsonify(address.__dict__)