-- Seed Initial Users
INSERT INTO users (username, email, role) VALUES 
('devops_admin', 'admin@uchicago.edu', 'admin'),
('test_user_01', 'user1@example.com', 'user'),
('test_user_02', 'user2@example.com', 'user')
ON CONFLICT (username) DO NOTHING;

-- Log the seeding event
INSERT INTO seed_log (action) VALUES ('Initial staging data seed successful');
