from flask import Blueprint, jsonify, request, make_response
from ..models.data import DataRecord, Sector, db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/last-record', methods=['GET'])
def get_last_record():
    last_record = DataRecord.query.order_by(DataRecord.id.desc()).first()
    if last_record:
        return jsonify(
            id=last_record.id,
            name=last_record.name,
            sectors=last_record.sectors,
            agree_to_terms=last_record.agree_to_terms
        )
    else:
        return jsonify(None)

@api_blueprint.route('/sectors', methods=['GET'])
def get_sectors():
    sectors = Sector.query.all()
    result = []

    for sector in sectors:
        sector_dict = {
            "id": sector.id,
            "name": sector.name,
            "subsectors": []
        }

        for subsector in sector.subsectors:  # Suponiendo que hay una relación en tu modelo Sector llamada 'subsectors'
            subsector_dict = {
                "id": subsector.id,
                "name": subsector.name
            }
            sector_dict["subsectors"].append(subsector_dict)

        result.append(sector_dict)

    return jsonify(result)

@api_blueprint.route('/submit', methods=['POST'])
def submit_data():
    user_data = request.json

    if not user_data.get("agree_to_terms"):
        return make_response(jsonify({"detail": "User must agree to terms."}), 400)

    record = DataRecord(
        name=user_data.get("name"),
        sectors=user_data.get("sectors"),
        agree_to_terms=user_data.get("agree_to_terms")
    )

    db.session.add(record)
    db.session.commit()

    return {"message": "Data saved successfully"}

@api_blueprint.route('/data/<int:record_id>', methods=['PATCH'])
def update_record(record_id):
    user_data = request.json

    if not user_data.get("agree_to_terms"):
        return make_response(jsonify({"detail": "User must agree to terms."}), 400)

    record = DataRecord.query.get(record_id)
    if not record:
        return make_response(jsonify({"detail": "Record not found."}), 404)

    record.name = user_data.get("name", record.name)
    record.sectors = user_data.get("sectors", record.sectors)
    record.agree_to_terms = user_data.get("agree_to_terms", record.agree_to_terms)

    db.session.commit()

    return jsonify(
        id=record.id,
        name=record.name,
        sectors=record.sectors,
        agree_to_terms=record.agree_to_terms
    )