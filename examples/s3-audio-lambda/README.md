### Step 1 - Create S3
1. Navigate to the S3 service.
2. Click **Create bucket** button.
3. Fill in the name.
4. Fill the region which will match lambda region.
5. All other fields are optional and additional, so you can leave as it is.
6. Click 'Create bucket' button.

### Step 2 - Create lambda function which is triggered by S3.
1. Navigate to the Lambda service.
2. Click **Create function** button.
3. Author from scratch.
4. Fill in the name and select Python 3.9 as runtime.
5. In the Permission tab expand Change default execution role.
6. Select Create a new role from AWS policy templates,
7. Fill in the name.
8. In Policy templates select Amazon S3 object read-only permissions.
9. Click **Create function** button.

### Step 3 - Add S3 trigger.
1. Now you are in the Lambda overview window.
2. On the Function overview click on **Add Trigger**.
3. Select source as S3.
4. Select your bucket.
5. Select **Event type** as **All object create event**.
6. Click on checkbox **I acknowledge that using the same S3 bucket for both input…**
7. Click Add.

### Step 4 - Edit lambda code.
1. Now you are back to the Lambda overview window.
2. Select **Code** tab and paste code from the GitHub repo.
3. Fill in all variables on the top of the lambda function code.
4. Click **Deploy**.

### View logs
1. In the Lambda overview page open **Monitor** tab.
2. Under it open **Logs** tab.
3. Click **View logs in CloudWatch**