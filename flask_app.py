
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import shodan

SHODAN_API_KEY = "priC0c2fKSobk4fnsT7xT76svsgGKziH"

api = shodan.Shodan(SHODAN_API_KEY)


ips = []
catch = {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def hello_world():
    if request.method == 'POST':
        counter = 0
        ips = []
        try:
            # Get input from form
            input = request.form.get('sstring')
            # Search Shodan
            results = api.search(input)
            # Show the results
            print('Results found: {}'.format(results['total']))
            for result in results['matches']:
                counter +=1
                if counter >= 1000:
                    break
                print('IP: {}'.format(result['ip_str']))
                catch['ip'] = result['ip_str']
                ips.append(result['ip_str'])
                print(result['data'])
                print('')
        except:
            print("Error")

        return render_template("home.html", ips = ips, catch = catch)

    else:    
        try:
            ips = []
            # Search Shodan
            results = api.search('apache')


            # Show the results
            print('Results found: {}'.format(results['total']))
            for result in results['matches']:
                    print('IP: {}'.format(result['ip_str']))
                    ips.append(result['ip_str'])
                    print(result['data'])
                    print('')
        except:
            print("Error")
        return render_template("home.html", ips = ips, catch = catch)


@app.route('/s1', methods=['GET', 'POST', 'PUT'])
def s1():
    try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
    except:
        print("Error")
    #return render_template("home.html", nr = results_number, catch = catch)
    return "Test";
