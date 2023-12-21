import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

def eda():
    st.sidebar.header("Visualizations")

    st.header("Upload your CSV data")
    data_file=st.file_uploader('Upload CSV',type=['csv'])

    if data_file is not None:
         data=pd.read_csv(data_file)
         st.write("Data Overview:")
         st.write(data.head())
         st.write(data.describe().T)

         plot_options= ["Bar Plot","Scatter Plot","Histogram","Box Plot"]
         selected_plot=st.sidebar.selectbox("Choose a Plot Type",plot_options)

         if selected_plot == "Bar Plot":
              x_axis=st.sidebar.selectbox('Select X-axis',data.columns)
              y_axis=st.sidebar.selectbox('Select y-axis',data.columns)
              st.write("Bar Plot")
              fig,ax=plt.subplots()
              sns.barplot(x=data[x_axis],y=data[y_axis],ax=ax)
              ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")  
              st.pyplot(fig)
         elif selected_plot=="Scatter Plot":
              x_axis=st.sidebar.selectbox("select x-axis",data.columns)
              y_axis=st.sidebar.selectbox("select y-axis",data.columns)
              st.write('Scatter Plot')
              fig,ax=plt.subplots()
              sns.scatterplot(x=data[x_axis],y=data[y_axis],ax=ax)
              st.pyplot(fig)
         elif selected_plot=="Histogram":
              column= st.sidebar.selectbox('Select a Column',data.columns)
              bins=st.sidebar.slider("Number of Bins",5,100,20)
              st.write("Histogram:")
              fig,ax=plt.subplots()
              sns.histplot(data[column],bins=bins,ax=ax)
              st.pyplot(fig)
         elif selected_plot=="Box Plot":
              column=st.sidebar.selectbox("select a column",data.columns)
              st.write("Boxplot")
              fig,ax=plt.subplots()
              sns.boxplot(data[column],ax=ax)
              st.pyplot(fig)
def input_data():
     BHK=st.slider(label="BHK",min_value=1,max_value=6,step=1)
     City=st.selectbox("City",('Kolkata', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad'))
     furnishing_Status=st.selectbox("Furnishing Status",('furnished','Semi-Furnished','Unfurnished'))
     tenant=st.selectbox('Tenant Preferred',('Bachelors/Family', 'Bachelors', 'Family'))
     bathroom=st.slider(label='Bathroom',min_value=1,max_value=7,step=1)
     point_c=st.selectbox("Point of Contact",('Contact Owner', 'Contact Agent'))
     rent_flr=st.slider(label='Rental Floor',min_value=-2,max_value=22,step=1)
     total_flr=st.slider(label='Total floor building',min_value=0,max_value=30,step=1)
     fixed_s=st.slider(label='Fixed Size',min_value=10,max_value=3100,step=10)
     sqft_r=st.slider(label='Sqft Rent',min_value=10,max_value=120,step=2)
     

     columns = ['BHK', 'City', 'FurnishingStatus', 'TenantPreferred', 'Bathroom',
           'PointofContact', 'RentalFloor', 'Totalfloorbuilding', 'FixedSize',
           'SqftRent']
     new_data = pd.DataFrame([[BHK, City, furnishing_Status, tenant, bathroom, point_c, rent_flr, total_flr, fixed_s, sqft_r]],
                              columns=columns)
     return new_data

def predict():
     st.write("""Predict rent of Apartment/House/Room""")
     with open("xgb_model.pkl","rb") as f:
          model=pickle.load(f)
     

     new_data = input_data()
     if st.button(label='Predict'):
        charges_pred = model.predict(new_data)
        charges=np.round(float(charges_pred[0]),2)
        st.success(f'Apartment Rent Estimate (INR): {charges}')

pages={'EDA':eda,'Predict':predict}

def main():
    st.title("Apartment_Price_Estimator & Exploratory Data Analysis")
    selected_page=st.sidebar.selectbox('Choose a page',options=list(pages.keys()))

    pages[selected_page]()

st.cache(allow_output_mutation=True)
if __name__ == '__main__':
	main()