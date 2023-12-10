<script setup>
  import { useTableDescription } from '@/stores/tableDescription.js';


  const tableDescriptionStore = useTableDescription();

  const params = {
    'index': 'Just an index of the row.',
    'observed': 'What was observed.',
    'location_details': 'The specific location of the sighting.',
    'county': 'The county in which the sighting occurred.',
    'state': 'The state in which the sighting occurred.',
    'season': 'The season in which the sighting occurred.',
    'title': 'The title of the sighting report.',
    'latitude': 'The latitude of the sighting.',
    'longitude': 'The longitude of the sighting.',
    'date': 'The date of sighting.',
    'number': 'The report number of the sighting.',
    'classification': 'All reports posted into the BFROs online database are assigned a classification: Class A, Class B, or Class C. The difference between the classifications relates to the potential for misinterpretation of what was observed or heard. A given witness might be very credible\, but could have honestly misinterpreted something that was seen, found, or heard. Thus, for the most part, the circumstances of the incident determine the potential for misinterpretation, and therefore the classification of the report. More can be seen in https://www.bfro.net/GDB/classify.asp.',
    'geohash': 'Geohash.',
    'temperature_high': 'Highest temperature for the day.',
    'temperature_mid': 'Average temperature for the day.',
    'temperature_low': 'Lowest temperature for the day.',
    'dew_point': 'Dew point on the day of sighting.',
    'humidity': 'Humidity on the day of sighting.',
    'cloud_cover': 'Cloudiness on the day of sighting.',
    'moon_phase': 'Moon phase of the day.',
    'precip_intensity': 'Percipation intensity.',
    'precip_probability': 'Percipation probability.',
    'precip_type': 'Percipation type.',
    'pressure': 'Pressure on the day of sighting.',
    'summary': '',
    'uv_index': 'Ultraviolet on the day of sighting.',
    'visibility': 'Visibility on the day of sighting.',
    'wind_bearing': 'Wind bearing on the day of sighting.',
    'wind_speed': 'Average wind speed on the day of sighting.'
  }
</script>
<template>
  <div id="table-block">
    <div id="params-block">
      <div class="param-btn" v-for="(value, key) in params">
        <img src="../assets/icechoose.svg"/>
        <p @click="tableDescriptionStore.setDescribeParam(key)">{{key}}</p>
      </div>
      <div class="blank-margin"/>
    </div>
    <div id="description-block">
      <p>{{ params[tableDescriptionStore.describeParam] }}</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
  #table-block {
    margin-top: 1rem;
    width: calc(100% - 40px);
    height: 230px;
    padding: 20px;
    background-color: #6176b6;
    border-radius: 7px;
  }
  #params-block {
    position: absolute;
    width: 320px;
    height: 230px;
    background-color: #f9fbff;
    overflow-y: scroll;
    border-radius: 7px;
    
    &::-webkit-scrollbar { width: 0; height: 0; }
    -ms-overflow-style: none;
    overflow: -moz-scrollbars-none;
    scrollbar-width: none;

    .param-btn {
      width: 304px;
      height: 74px;
      background-color: #f9fbff;
      border-radius: 7px;
      margin-left: 8px;
      margin-top: 20px;
      img {
        height: 100%;
        width: 100%;
        filter: drop-shadow(0px 5px 5px #4e5f92);
      }
      p {
        position: relative;
        width: 100%;
        margin-top: -60px;
        text-align: center;
        font-family: 'Fugaz One', serif;
        font-size: 1.5rem;
        color: #e6edfe;
        font-weight: 600;
        cursor: pointer;
        filter: drop-shadow(1px 1px 3px #4e5f92);

        transition: all 0.1s ease-in-out; 
        &:hover {
          font-size: 1.5rem;
          margin-top: -63px;
          filter: drop-shadow(1px 1px 5px #26345c);
        }
      }
    }
    
    .blank-margin {
      height: 25px;
    }
  }
  #description-block {
    position: relative;
    background-color: #e6edfe;
    overflow-y: scroll;
    border-radius: 7px;
    width: calc(100% - 380px);
    padding-left: 20px;
    padding-right: 20px;
    height: 100%;
    margin-left: 340px;

    &::-webkit-scrollbar { width: 0; height: 0; }
    -ms-overflow-style: none;
    overflow: -moz-scrollbars-none;
    scrollbar-width: none;

    p {
      margin: 0;
      margin-top: 1rem;
      font-family: 'Fugaz One', serif;
      font-size: 1.1rem;
      color: #464c5f;
      font-weight: 600;
    }
  }

  @media (max-width: 1000px) {
    #table-block {
      width: auto;
      height: 500px;
    }
    #params-block {
      position: relative;
      width: 100%;
      height: 170px;

      .param-btn {
        width: 250px;
        margin-left: calc(50% - 125px);
        margin-top: 5px;
      }
    }
    #description-block {
      position: relative;
      width: auto;
      height: 310px;
      margin-left: 0;
      margin-top: 20px;
    }
    .blank-margin {
      height: 5px;
    }

  }
</style>
