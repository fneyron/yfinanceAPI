from flask import Flask, jsonify, request
import yfinance as yf

app = Flask(__name__)


@app.route('/historical-data', methods=['GET'])
def get_historical_data():
    symbol = request.args.get('symbol')
    period = request.args.get('period', '1mo')  # default to 1 month
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    hist = data.history(period=period)
    return jsonify(hist.to_dict())


@app.route('/dividends', methods=['GET'])
def get_dividends():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    div = data.dividends
    return jsonify(div.to_dict())


@app.route('/splits', methods=['GET'])
def get_splits():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    splits = data.splits
    return jsonify(splits.to_dict())


@app.route('/info', methods=['GET'])
def get_info():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    info = data.info
    return jsonify(info)


@app.route('/balance-sheet', methods=['GET'])
def get_balance_sheet():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    balance_sheet = data.balance_sheet
    return jsonify(balance_sheet.to_dict())


@app.route('/cash-flow', methods=['GET'])
def get_cash_flow():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    cash_flow = data.cashflow
    return jsonify(cash_flow.to_dict())

@app.route('/earnings', methods=['GET'])
def get_earnings():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    earnings = data.earnings
    return jsonify(earnings.to_dict())

@app.route('/financials', methods=['GET'])
def get_financials():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400

    data = yf.Ticker(symbol)
    financials = data.financials
    return jsonify(financials.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
