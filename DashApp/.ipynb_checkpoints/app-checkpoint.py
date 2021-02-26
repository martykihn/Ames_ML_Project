{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash_core_components as dcc\n",
    "import dash_html_components as html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = dash.Dash()\n",
    "colors = {\n",
    "    'background': '#111111',\n",
    "    'text': '#7FDBFF'\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "app.layout = html.Div(style={'backgroundColor': colors['background']}, \\\n",
    "                            children = [\n",
    "    html.H1(\n",
    "        children = 'Hello Dash',\n",
    "        style = {\n",
    "            'textAlign': 'center',\n",
    "            'color': colors['text']\n",
    "        }\n",
    "    ),\n",
    "    html.Div(children = 'Dash: A web app framework for Python', \\\n",
    "            style = {\n",
    "        'textAlign': 'center',\n",
    "        'color': colors['text']\n",
    "    }),\n",
    "    dcc.Graph(\n",
    "        id='Graph1',\n",
    "        figure = {\n",
    "            'data': [\n",
    "                {'x': [1, 2, 3], 'y': [4, 1, 2], \\\n",
    "                'type': 'bar', 'name': 'SF'},\n",
    "                {'x': [1, 2, 3], 'y': [2, 4, 5], \\\n",
    "                'type': 'bar', 'name': 'Montreal'},\n",
    "            ],\n",
    "            'layout': {\n",
    "                'plot_bgcolor': colors['background'],\n",
    "                'paper_bgcolor': colors['background'],\n",
    "                'font': {\n",
    "                    'color': colors['text']\n",
    "                }\n",
    "            }\n",
    "        }\n",
    "    )\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
