-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create the ads table
CREATE TABLE IF NOT EXISTS ads (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    category VARCHAR(100),
    location VARCHAR(200),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes
CREATE INDEX idx_ads_category ON ads(category);
CREATE INDEX idx_ads_title ON ads(title);
CREATE INDEX idx_ads_created_at ON ads(created_at DESC);

-- Add sample data
INSERT INTO ads (title, description, price, category, location, contact_email, contact_phone)
VALUES 
    ('Gaming Laptop Pro', 'RTX 4080, 32GB RAM, 1TB SSD', 1499.99, 'Electronics', 'San Francisco', 'seller1@example.com', '+1-555-0101'),
    ('Ergonomic Office Chair', 'Premium mesh chair with lumbar support', 299.99, 'Furniture', 'New York', 'seller2@example.com', '+1-555-0102'),
    ('MacBook Pro M3 Max', '36GB RAM, 1TB SSD, 16-inch', 2499.99, 'Electronics', 'Los Angeles', 'seller3@example.com', '+1-555-0103'),
    ('Standing Desk', 'Electric height adjustable', 499.99, 'Furniture', 'Chicago', 'seller4@example.com', '+1-555-0104'),
    ('Wireless Headphones', 'Noise cancelling, 40hr battery', 199.99, 'Electronics', 'Miami', 'seller5@example.com', '+1-555-0105')
ON CONFLICT DO NOTHING;
