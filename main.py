import PySimpleGUI as sg

layout = [
  [
      sg.Input( key = 'Input'),
sg.Spin(['KM to Mile', 'KG to Pound', 'SEC to MIN'], key = 'Units'),
sg.Button('Convert', key = 'Convert')],
    [sg.Text('Output', key = 'OUTPUT')]
          ]
window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Convert':
        input_value=values['Input']
        if input_value.isnumeric():
            print(input_value)
            match values['Units']:
                case 'KM to Mile':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f'{input_value} Km are {output} miles.'

                case 'KG to Pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} Kg are {output} pounds.'

                case 'SEC to MIN':
                    output = round(float(input_value) /60, 2)
                    output_string = f'{input_value} seconds are {output} mins.'

            window['OUTPUT'].update(output_string)
        else:
            window['OUTPUT'].update('Please enter a number')


window.close()