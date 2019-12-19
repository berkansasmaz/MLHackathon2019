<template>
	<div>
		 <page-head icon="pen" title="Comment" />
		<div class="text-center">
			<mli-text title="Link" placeholder = "Lütfen yorum çekmek istediğiniz linki giriniz" v-model="pageLink"></mli-text>
			<button v-if="pageLink" @click="get" class="btn btn-primary">
					<icon icon="plus"/>	Get
			</button>
		</div>

		<!-- Content -->
          <div class="container-fluid flex-grow-1 container-p-y">

            <h4 class="d-flex justify-content-between align-items-center w-100 font-weight-bold py-3 mb-4" v-if="olumluYorumlar.length != 0">
              <div>OLUMLU YORUMLAR</div> 
            </h4>


            <div class="card" v-if="olumluYorumlar.length != 0">
              <div class="card-datatable table-responsive">
                <table class="table table-striped table-bordered">
                  <thead class="thead-dark">
                    <tr>
					<th >#</th>
					<th >Yorum</th>
                    </tr>
                  </thead>
				  <tbody v-for="(item, index) in olumluYorumlar" :key="index" class="table-dark">
					  <tr>
						  <td>{{index}}</td>
						  <td>{{item}}</td>
					  </tr>
				  </tbody>
                </table>
              </div>
            </div>
          </div>
          <!-- / Content -->
		  <!-- Content -->
          <div class="container-fluid flex-grow-1 container-p-y">

            <h4 class="d-flex justify-content-between align-items-center w-100 font-weight-bold py-3 mb-4"  v-if="olumsuzYorumlar.length != 0">
              <div>OLUMSUZ YORUMLAR</div> 
            </h4>


            <div class="card" v-if="olumsuzYorumlar.length != 0">
              <div class="card-datatable table-responsive">
                <table class="table table-striped table-bordered">
                  <thead class="thead-dark">
                    <tr>
					<th >#</th>
					<th >Yorum</th>
                    </tr>
                  </thead>
				  <tbody v-for="(item, index) in olumsuzYorumlar" :key="index" class="table-dark">
					  <tr>
						  	<td>{{index}}</td>
						  <td>{{item}}</td>
					  </tr>
				  </tbody>
                </table>
              </div>
            </div>
          </div>
          <!-- / Content -->
	</div>
</template>

<script>
  	import service from "service/MLHackathonServer";
  import router from "@/router";
export default {

  data() {
    return {
	  olumluYorumlar: [],
	  olumsuzYorumlar: [],
	  pageLink: ""
    }
  },
    methods: {
	   async get(){
				var olumsuz = await service.olumsuzList(this.pageLink);
					console.log(olumsuz);
					this.olumsuzYorumlar = olumsuz;		
				var olumlu = await service.olumluList(this.pageLink);
					console.log(olumlu);
					this.olumluYorumlar = olumlu
		},
	}
//    watch: {
//     '$route': 'fetchData'
//   }
}
</script>