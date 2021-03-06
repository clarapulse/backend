CREATE TABLE [users] (
  [user_id] string PRIMARY KEY
)
GO

CREATE TABLE [connections] (
  [connection_id] string PRIMARY KEY,
  [user_id_one] string,
  [user_id_two] string
)
GO

ALTER TABLE [connections] ADD FOREIGN KEY ([user_id_one]) REFERENCES [users] ([user_id])
GO

ALTER TABLE [connections] ADD FOREIGN KEY ([user_id_two]) REFERENCES [users] ([user_id])
GO
