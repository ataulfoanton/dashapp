from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

# Relevant features
client_info_cols = [
    'CODE_GENDER',
    'FLAG_OWN_CAR',
    'AMT_INCOME_TOTAL',
    'NAME_TYPE_SUITE',
    'NAME_INCOME_TYPE',
    'NAME_EDUCATION_TYPE',
    'NAME_FAMILY_STATUS',
    'NAME_HOUSING_TYPE',
    'AGE_YEARS',
    'YEARS_EMPLOYED',
    'OCCUPATION_TYPE',
    'ORGANIZATION_TYPE'
]
loan_info_cols = [
    'NAME_CONTRACT_TYPE',
    'AMT_CREDIT',
    'AMT_ANNUITY',
    'AMT_GOODS_PRICE'
]
elements_info_cols = [
    'FLAG_DOCUMENT_2',
    'FLAG_DOCUMENT_3',
    'FLAG_DOCUMENT_4',
    'FLAG_DOCUMENT_5',
    'FLAG_DOCUMENT_6',
    'FLAG_DOCUMENT_7',
    'FLAG_DOCUMENT_8',
    'FLAG_DOCUMENT_9',
    'FLAG_DOCUMENT_10',
    'FLAG_DOCUMENT_11',
    'FLAG_DOCUMENT_12',
    'FLAG_DOCUMENT_13',
    'FLAG_DOCUMENT_14',
    'FLAG_DOCUMENT_15',
    'FLAG_DOCUMENT_16',
    'FLAG_DOCUMENT_17',
    'FLAG_DOCUMENT_18',
    'FLAG_DOCUMENT_19',
    'FLAG_DOCUMENT_20',
    'FLAG_DOCUMENT_21'
]
features = client_info_cols + loan_info_cols + elements_info_cols

loan_score = html.Div(
    [
        dbc.Row(
            [
                html.Div(id='title'),
                html.Div(id='decision')
            ],
            className='mb-2'
        ),
        dbc.Row(
            dcc.Graph(id='gauge-score')
        ),
        dbc.Row(
            [
                dcc.Graph(id='impact_pos'),
                dcc.Graph(id='impact_neg')
            ]
        )
    ]
)

file_details = html.Div(
    [
        dbc.Row(
            [
                html.H3('File details'),
                # html.Div(id='decision')
            ],
            className='mb-2'
        ),
        dcc.RadioItems(
            id='buttons',
            options=[
                {'label': 'Client data', 'value': 'information'},
                {'label': 'Characteristics of loan', 'value': 'characteristics'},
                {'label': 'File elements', 'value': 'elements'}
            ],
            value='information',
            inline=True,
            inputStyle={'margin-left': '50px'},
            style={'textAlign': 'right'},
            className='mb-3'
        ),
        dash_table.DataTable(
            id='table',
            columns=[{'id': i, 'name': i} for i in ['Feature', 'Value']],
            style_cell={'color': 'black', 'width': 'auto'}
        )
    ]
)

general_performance = html.Div(
    [
        dbc.Row(
            [
                dbc.Label('Feature:'),
                dcc.Dropdown(
                    id='feature',
                    options=[
                        {'label': feat, 'value': feat} for feat in features
                    ],
                    style={'color': 'black'}
                )
            ],
            className='mb-3'
        ),
        dbc.Row(
            dcc.Graph(id='general-performance')
        )
    ]
)
