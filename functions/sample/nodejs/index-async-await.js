/**
 * Get all dealerships
 */

const { Cloudant } = require('@cloudant/cloudant');
//const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
      //const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
      const cloudant = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY }
      });
      
      try {
        let dbList = await cloudant.db.list();
        return { "dbs": dbList };
      } catch (error) {
          return { error: error.description };
      }
}

