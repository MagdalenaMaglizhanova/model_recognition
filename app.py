from flask import Flask, render_template, request, jsonify
from pyswip import Prolog

app = Flask(__name__)
prolog = Prolog()

# Добавяне на коли
prolog.assertz("car('tesla_model_s', 'Tesla Model S', 'An all-electric luxury sedan known for its high performance, long range, and cutting-edge technology.')")
prolog.assertz("car('ford_mustang', 'Ford Mustang', 'An iconic American muscle car known for its aggressive design and powerful V8 engine.')")
prolog.assertz("car('toyota_corolla', 'Toyota Corolla', 'A reliable and fuel-efficient compact car that is one of the best-selling vehicles in the world.')")
prolog.assertz("car('bmw_m3', 'BMW M3', 'A high-performance sports sedan from BMW''s M division, praised for its speed and handling.')")
prolog.assertz("car('audi_r8', 'Audi R8', 'A luxury sports car featuring a V10 engine and sleek design, offering both style and speed.')")
prolog.assertz("car('chevrolet_camaro', 'Chevrolet Camaro', 'A classic American muscle car known for its bold styling and strong performance.')")
prolog.assertz("car('porsche_911', 'Porsche 911', 'A legendary sports car recognized for its timeless design and precise engineering.')")
prolog.assertz("car('mercedes_benz_g_class', 'Mercedes-Benz G-Class', 'A luxury SUV with iconic boxy design, combining off-road capability with comfort.')")
prolog.assertz("car('honda_civic', 'Honda Civic', 'A practical and popular compact car known for reliability, fuel efficiency, and value.')")
prolog.assertz("car('jeep_wrangler', 'Jeep Wrangler', 'A rugged SUV built for off-road adventures, known for its removable doors and roof.')")
prolog.assertz("car('lamborghini_aventador', 'Lamborghini Aventador', 'A high-performance supercar with striking looks and a powerful V12 engine.')")
prolog.assertz("car('ferrari_488', 'Ferrari 488', 'A sleek Italian supercar featuring aerodynamic design and blistering speed.')")

# Списък с изображения за колите
car_images = {
    'tesla_model_s': 'car1.png',
    'ford_mustang': 'car2.png',
    'toyota_corolla': 'car3.png',
    'bmw_m3': 'car4.png',
    'audi_r8': 'car5.png',
    'chevrolet_camaro': 'car6.png',
    'porsche_911': 'car7.png',
    'mercedes_benz_g_class': 'car8.png',
    'honda_civic': 'car9.png',
    'jeep_wrangler': 'car10.png',
    'lamborghini_aventador': 'car11.png',
    'ferrari_488': 'car12.png'
}

@app.route('/')
def chat_page():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400

        print(f"Получено съобщение: {user_message}")

        result = []
        image_name = None

        # Проверка дали съобщението съдържа име на кола
        for entity, img in car_images.items():
            if entity in user_message.lower():
                result = list(prolog.query(f"car('{entity}', Name, Description)."))
                image_name = img
                break

        if result:
            return jsonify({'response': result[0]['Description'], 'image': image_name})

        return jsonify({'response': "Не разбирам въпроса."})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
