# TradePilot - Vendor Management System (Django Backend)

## Introduction

TradePilot is a Vendor Management System (VMS) built on the Django web framework with Django Rest Framework for efficient API development. This project aims to streamline vendor-related operations and management within your organization.

## Overview
TradePilot is designed to simplify vendor management, procurement, and performance tracking, allowing your business to operate efficiently. With this API, you can perform the following key tasks:

- **Vendor Creation:** Easily create, retrieve, update, and delete vendor information.Manage essential vendor details, contacts, and relationships.

- **Purchase Order Management:** Generate and track purchase orders for various products and services. Efficiently handle the procurement workflow with customizable order parameters.
- **Performance Metrics:** Monitor vendor performance metrics, including on-time delivery rates.Gain insights into the reliability and efficiency of your vendor network.

## Requirements

- Python 3.11.2
- Django 5.0
- Django Rest Framework 3.14.0

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Overwatch0812/TradePilot
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Apply database migrations:

   ```bash
   python manage.py migrate
4. python manage.py runserver:

   ```bash
   python manage.py runserver

## API Endpoints

- **Vendor related (here pk stands for primary key which is the id of vendor):**

    1. Vendor list: **"/api/vendors/"**, HTTP method:GET, used to display all the vendors in tha database.
    2. Vendor Creation: **"/api/vendors/create/"**, HTTP method:POST, used to create new vendor.
    3. Vendor Details: **"/api/vendors/<int:pk>/detail/"**, HTTP method:GET, used to view the details of a particular vendor.
    4. Vendor Creation: **"/api/vendors/<int:pk>/update/"**, HTTP method:PUT, used to update the details of a vendor.
    5. Vendor Creation: **"/api/vendors/<int:pk>/delete/"**, HTTP method:DELETE, used to delete a vendor.

- **Purchase order related:**

    1. Purchase order list of a particular vendor: **"/api/purchase_order/int:pk>/"**, HTTP method:GET, used to display all the purchase order of a particular vendor in tha database("pk is primary key, i.e, id of a vendor).
    2. Purchase order Creation: **"/api/purchase_order/create/"**, HTTP method:POST, used to create new Purchase order.
    3. Purchase order Details: **"/api/purchase_order/<int:pk>/detail/"**, HTTP method:GET, used to view the details of a particular Purchase order("pk is primary key, i.e, id of a purchase order).
    4. Purchase order Creation: **"/api/purchase_order/<int:pk>/update/"**, HTTP method:PUT, used to update the details of a Purchase order("pk is primary key, i.e, id of a purchase order).
    5. Purchase order Creation: **"/api/purchase_order/<int:pk>/delete/"**, HTTP method:DELETE, used to delete a Purchase order("pk is primary key, i.e, id of a purchase order).

- **Performance related:**

  Collection of performance measure of a particular vendor: **"/api/vendors/<int:pk>/performance/"**, HTTP method:GET, retrieves the calculated performance metrics for a specific vendor("pk is primary key, i.e, id of a vendor).

- **Acknowledge a purchase order:**

  Acknowledgement of a purchase order: **"/api/purchase_order/<int:pk>/acknowledge/"**, HTTP method:GET,  an endpoint like for vendors to acknowledge Purchase order("pk is primary key, i.e, id of a purchase order).

## Additional Information:

- **Real-time Updates:** Django signals has been used to trigger metric updates in real-time when related PO data is modified.
- **Authorization and Authentication:** Token Authentication is used to establish and maintain secure means of communication between frontend and backend.
- **Deployment and Hosting:** Hosted on Vercel and ready to use.
- **Testing:** Tested with the help of Postman Tool.


