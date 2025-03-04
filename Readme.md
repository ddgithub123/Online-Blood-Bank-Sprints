# Blood Donation Platform

This project is a backend system for managing blood donation operations, connecting donors, recipients, and healthcare organizations. The system handles user management (Donors, Recipients, and Organizations), blood donation tracking, request management, and donation camp scheduling.

## Features

- **User Management**: The system supports three types of users:
  - **Donors**: Can donate blood and track donation history.
  - **Recipients**: Can request blood and track request statuses.
  - **Organizations (Hospitals)**: Manage blood inventory, blood requests, and organize blood donation camps.

- **Blood Request Management**: Recipients can place blood requests based on their blood type, urgency, and quantity. Hospitals/organizations can fulfill these requests and track their status.

- **Donation History**: Donors can track their donation history, including blood type donated, quantity, and donation date.

- **Donation Camps**: Organizations can schedule donation camps, and donors can register to attend.

- **Real-time Inventory Management**: Blood inventory is managed by hospitals/organizations and can be updated as donations are made.

## Project Structure

### Models

The system includes the following models:

- **User**: Represents the base user model for Donors, Recipients, and Organizations.
- **Donor**: Represents a blood donor and their donation history.
- **Recipient**: Represents a recipient who needs blood.
- **Organization (Hospital)**: Represents a healthcare organization managing blood requests and donations.
- **BloodRequest**: Represents a request for blood made by a recipient or a hospital.
- **BloodDonation**: Represents a blood donation made by a donor.
- **BloodBank**: Represents a blood bank storing donated blood.
- **DonationCamp**: Represents a scheduled blood donation camp managed by an organization.

### Relationships

The relationships between the models are as follows:

- **User**: Base model for Donors, Recipients, and Organizations.
- **Donor** has a One-to-One relationship with **User**.
- **Recipient** has a One-to-One relationship with **User**.
- **Organization** has a One-to-One relationship with **User**.
- **BloodRequest** is linked to **Recipient** and **Organization** (Foreign Keys).
- **BloodDonation** is linked to **Donor** and **BloodBank** (Foreign Keys).
- **DonationCamp** is linked to **Organization**.

### Models Overview

1. **User**: The base model containing user info such as name, email, phone, and role (Donor, Recipient, or Organization).
2. **Donor**: Contains additional fields for blood group, medical history, donation history, and eligibility.
3. **Recipient**: Contains information like blood group, medical history, and request status.
4. **Organization**: Contains details about hospitals/organizations, blood inventory, and their scheduled donation camps.
5. **BloodRequest**: Stores the details of blood requests placed by recipients or hospitals.
6. **BloodDonation**: Tracks donations made by donors, including the blood type and quantity donated.
7. **BloodBank**: Stores available blood units in the system, including their quantities and types.
8. **DonationCamp**: Represents a donation camp event with a scheduled date, location, and targeted blood types.

## Installation

To set up this project locally, follow the steps below.

### Prerequisites

- Python 3.8+
- Django 3.2+
- MongoDB or PostgreSQL (you can modify for other databases)
- pip (for installing dependencies)

### Setup Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/blood-donation-platform.git
   cd blood-donation-platform
