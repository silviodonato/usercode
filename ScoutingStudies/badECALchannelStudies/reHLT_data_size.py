import FWCore.ParameterSet.Config as cms

## from environment variable
import os
badChannels_level = int(os.environ['NOCHANNELS_LEVEL'])


fileList = [
#'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/00377874-82bc-49b5-9210-4df624280b4a.root',

'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/48f28039-0de0-48ed-bb4b-8764e2da928b.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/4a5b73cb-df84-4d80-b934-9f8fd7ac42a5.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/4b4711b2-fff8-422b-9957-40a093fbef2e.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/4b998839-ede9-4ba9-bee5-00098e1bc785.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/4cf57ba6-d61d-41f1-adf8-27fd0a16b34e.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/4d5cd2db-69f4-4b83-ad8e-46300609417a.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/4df45300-4e74-4d72-a8ae-9f5d95bdb89d.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5071571c-55cc-49b9-8078-c7e6bf297686.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/508095ef-e5de-4422-b6d0-478fca1cdeca.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/513bb780-c683-4029-9b7f-d1ecc9e4e647.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/52199eac-33f7-4691-8e9f-643408c876dd.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/53425ab5-ba88-4000-a455-651646b49438.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/54cd1f80-1c0d-47ee-94ee-4991f1b51e93.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/56405ed2-890d-4123-a8ee-a4f2142373b2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5713895b-bc96-4095-863b-ea47388d6387.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5a196900-28c2-44ce-8b3c-eb20f34ae7a9.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5a1f9b60-b18c-4445-b7fa-278d5d216fcb.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5aad54e9-1d26-48ad-8f17-f0cafce814c5.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5aff6373-8033-4b1b-9d87-e1317dc55874.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5c24626e-2292-44ce-809c-fad4c7b51235.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5d15edc8-4d91-4b99-a553-2a2bd32a6abf.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5f3a6bfe-9fd2-4799-8453-6c1638a06fa1.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/5fdd8f0c-5de2-44da-a466-6d113d0b92b9.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6036535f-af78-42e4-9ca2-b64d3cb474d2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6156051f-a96f-4e73-a5c1-9f1b4a328cdf.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/61a9cdcf-ee4e-4000-8a16-2c2357d9caeb.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/655265b6-fc32-4c81-aa37-37c1d05f1977.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/659e5a0d-b3a4-4d02-9d24-018b08aae597.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6765be77-946f-4d75-a044-dc1a2454e846.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/683b56c5-e778-4a65-8522-e33b52b00285.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6a9e9741-7c70-4679-944b-18a3115350b2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6c80a078-8bef-4410-9b7f-4e809db1b3ad.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6d1894c5-412d-4a03-8b46-477507175125.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/6f0e8d65-2c4c-49ca-9924-3d49a5f8c246.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/71d68ac4-1080-44cb-8c1c-d89ede7f986e.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/72770881-037e-4243-9d9c-81cdbe121de8.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/7384b210-736c-4aca-8242-196ae733f0bd.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/741367b7-fa4b-4e29-956a-7b277bc7fddf.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/758eefd7-9ee1-4752-a197-7dc0ad7cf6e2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/7668f525-b32a-46cf-8e47-716d42751e91.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/780b1f40-f3c0-4f43-9cbb-7c1770da2466.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/7bd33908-4020-47d2-bb3d-f6fdb1e4b732.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/7c021d39-fbbe-4bd9-b4c1-fd31f3266490.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/7def983a-801f-44cd-8b8c-9f7a88548ec2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/80301a3f-49cc-421c-a892-a5182da19295.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/808c0312-6ced-4cdd-b118-aefe056e3f47.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/817db68e-6835-46d9-86df-12fb54f49e16.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/81acb6aa-e1cc-4916-8538-a710d8be8ce6.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/82b3a6ba-9280-4bc1-b0ab-a5fd1cc1d932.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/84ff7330-09ff-4241-878b-01b6b2b64768.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/853c9d68-a8d1-4723-9614-3e3c799ed061.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/85dedcd0-d182-4076-aa1f-d8d2e9547605.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/86e4a0ec-1616-4c58-acb4-7e5101ed4a3e.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/873e73d7-5f65-4243-8d95-1b54b32c893a.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/8811f3cd-e72c-4d87-916c-65c386eec914.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/884596bc-608f-46c7-ab30-770434b57cfb.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/88784801-1981-47d1-8341-de24bbefcd92.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/887e3ea5-c4d5-4253-8f77-90f1e22279ed.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/88a76460-854a-4272-ad60-daba094c6e08.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/8dc740f6-617d-446b-8172-a6e2abddc3f2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/8e4bc942-87af-48db-8043-9d50841c69b0.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/8f0e4766-5861-45ec-b7ca-fb3a60b18ced.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/8f7045ed-e2c2-4d8f-bba6-cfeea8a45177.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/8fd03efc-4208-43df-8aa5-1f9831dd4761.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9015c584-c2d1-41e3-8f32-7c82812cd395.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9137d6e0-79eb-4d5d-b942-14c93e462130.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/97413768-fdbd-48e9-b1ce-64017e05edb0.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/978c715d-fe23-48a5-a09b-1bdd91e4dfde.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9804aaf7-f43e-4ccc-ae3b-0ee027cdf9e5.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/98771e85-378d-4d2c-b3b9-39db7558a14d.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9938615d-810a-4c52-9c74-a1a6565612d0.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/999f00d3-8a4f-440b-b87e-1337c9dde258.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9a5193ed-1206-4b79-b6fe-fcfeccbbaeb2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9a96b059-55cc-4289-97c3-fee318a3a5d3.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9c378d81-a450-4edf-8880-b425694415f1.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/9ce149ce-b618-4eca-86ef-2847111cd04f.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/a00cf661-db8e-418b-a544-e1cee3657973.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/a2777be6-55f9-45cd-a63e-aa8e78db2bb7.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/a4fa67aa-f7ba-4152-800c-8ec523005b96.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/a630794d-9a67-4d56-bf3e-c4c4aff6a7a9.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/a90882e1-92d1-4508-ac87-2beed864d9fc.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/a9f2e944-4b8e-42c9-a0e9-aa60e091f5eb.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/aa03c8d8-c418-40cc-9c8a-54fc2cf9e701.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/aa1aeb13-9978-4b83-a30e-e6eeb809a08f.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ab6fa546-04ae-4291-b2cd-054f4b956404.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ac9ddd7e-8a92-4ed9-a306-dfe74ffaab35.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/acca3cff-e145-4342-bc00-4cc141aba5af.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/add5a858-9bc6-486d-b4d9-a5397182b5b2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ae608bbb-eeab-4cfc-86c8-1da9496d76c2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ae747076-043e-4de0-86da-16746dbc02b2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ae8f02a6-eaf9-434e-b80b-38430de38a91.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ae99d4ac-ea7a-4b01-bf8e-6ab7c1d17045.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ae9f5cf1-5025-41b9-b863-ee115f640a72.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/af0dfa7b-bda8-4238-bb52-b7c4ea3ce965.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/afd3b2aa-bcda-480e-b3e7-26a4bd5e6de7.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b0765bd2-b757-4747-9ff5-52dbe364f098.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b2e55e3d-4166-42a3-aa61-d3b27696614c.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b31c8ac4-a072-4f77-9bec-bc92affa11f2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b522871b-a64b-4a1d-9c1b-bf2bcda5a39c.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b5fe9ac5-c223-41e1-a636-936ec4c8518b.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b7012289-5c07-4e5b-a33a-588dbc2cf814.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b705cb34-b0d2-4ec1-b2bb-83e25594f118.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b84c1cd8-ca53-48df-9fe1-62ea3625dd08.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b952b9a3-aacb-4140-a1a5-b0534e4cdba4.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/b9a1f027-8f43-4adc-b84c-dab3ffc14285.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/babded5b-627c-4970-8475-63538bea50f8.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/bb0f0935-1ac5-4d04-b200-12d8ee2c2c9b.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/bc7a2f1d-ec0e-4496-a680-d07eeff8c325.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/bde4dd71-ce52-4750-9e5e-e3c74f9161e5.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/bef662f6-015f-4c8b-a082-9acca073fd52.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/bf78a7df-19ca-459c-91ab-929a65bb0302.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/bffd52ab-2932-41a8-96e8-e13385480e0a.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c2916796-d9a6-4d1d-82e8-ab47e893c010.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c3386c60-4f79-4925-989b-c340b90d49a1.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c41cc065-5445-476f-9e12-4361a9825e47.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c4919caa-c2a9-4733-9dae-621cc4cb0bcf.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c4c3c8d3-b7e3-4a09-a53b-b8154f4baf98.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c75c6b7f-6516-408f-9419-1a9ac305b34c.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/c904ff3b-987f-4fa5-919b-3a724e70a914.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cb01614f-776b-4f70-a077-df2ab112d4a1.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cbb9bf76-fe97-4cd9-8a76-61b0f6ee8edd.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/ccbed0f2-caba-4c66-a699-c7f535b3607c.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cd09911a-4cf1-40cc-8417-a0089284055b.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cd155d86-8e9f-40e0-940d-9ae4009b8033.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cd31403c-a9b0-46ec-b09a-d8e99a67eb86.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cd4cd199-1a9a-43e4-bc56-c3a862c31d8c.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cd8c0cbe-1ce3-4d19-884a-2571384fffd6.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/cde70aa4-0fe6-4bac-b31f-0a868d175076.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d086f04a-26f9-4773-80be-14bc1084ab53.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d1a933c9-51fb-4051-8843-22be58809a2a.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d242c52f-5de2-4193-a8ea-e7649c53f8d2.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d2eb044a-dedd-4bdb-81a3-80cebe28fea1.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d3005684-10ac-4d10-95c4-625305f58bc7.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d3384431-a180-4a74-80c4-079d66a17e9f.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d7866b39-755c-4de7-8458-d4a3e5c026f7.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d7a6246b-3dd0-40d0-ac20-42dfd04b6aac.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d8262da2-3398-49ae-87fd-e7069c610d8f.root',
'/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/d84e84d6-3193-41f1-ba5d-05f46c3d21c7.root', 
]

for i, file in enumerate(fileList):
    fileList[i] = 'file:' + file.replace("/eos/cms/store/data/Run2025E/EphemeralHLTPhysics7/RAW/v1/000/396/102/00000/","/scratch/sdonato/data/00000/")

from reHLT_data import process

del process.hltOutputScoutingPF0
del process.DQMOutput

badChannels = [
    'kNoisy', #molto bene
    'kDAC', # bene
    'kFixedG0', #bene
    'kFixedG6', #benino
    'kNoDataNoTP', #malino
    'kDeadVFE', #male
    'kNonRespondingIsolated', #male
    'kFixedG1', #male
    'kDeadFE', #benino
    'kNNoisy', #malissimo
]

#badChannels=list(reversed(badChannels))
badChannels = badChannels[:badChannels_level]
print("Bad channels from command line:", badChannels)

process.hltEcalRecHit.ChannelStatusToBeExcluded = badChannels

process.maxEvents.input = 10000

process.source.fileNames = fileList

## to string nokDAC_kNoisy_kNNoisy_kFixedG6_kFixedG1_kFixedG0_kNonRespondingIsolated_kDeadVFE_kDeadFE_kNoDataNoTP ...
tag = "no"
for el in process.hltEcalRecHit.ChannelStatusToBeExcluded:
    tag += el.replace('k','') + "_"


process.hltOutputScoutingPF1.fileName = f'out_ECAL_{tag}.root'

process.options.numberOfThreads = 12
