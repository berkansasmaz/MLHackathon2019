<template>
	<div>
		 <page-head icon="chart-line" title="Model" />
		<div class="text-center">
			<mli-text title="Metin" placeholder = "Lütfen analiz yapılmasını istediğiniz metni giriniz" v-model="metin"></mli-text>
			<button  @click="post" class="btn btn-primary">
					<icon icon="chart-line"/>	Duygu Analizi
			</button>
		</div>
	<div v-if="sonuc.lenght != 0">
		<p v-if="sonuc[0] == 0">
			Olumsuz
		</p>
				<p v-if="sonuc[0] == 1">
			Olumlu
		</p>
	</div>
	</div>
</template>

<script>
import axios from "axios";
import Vue from 'vue';
const formData = new FormData();
 const httpFormData = axios.create({
  headers: {
	'Content-Type': 'multipart/form-data',
    "X-Requested-With": "XMLHttpRequest",
	"X-Application-Name": "vue"
  }
});
import router from "@/router";
import service from "service/MLHackathonServer";


export default {

  data() {
    return {
		sonuc: [],
		metin: ""
    }
  },
    methods: {
	   async post(){
		   formData.append('data', this.metin);

				  var result = await httpFormData.post("http://127.0.0.1:5000/predict", formData);
				console.log(result.data);
				this.sonuc = result.data;
							this.$router.go(0);
		},

	}
}
</script>