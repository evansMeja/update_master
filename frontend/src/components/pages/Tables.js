import React from "react";
import $ from 'jquery';

async function fetchDataAsync() {
  const response = await fetch('http://127.0.0.1:8000/api/api-data/');
  var json_r = await response.json()
  console.log();
  for(var i=0;i<json_r.length;i++){
      var textString =' <tr> <td>'+json_r[i][0].fields.oem_id+'</td><td> '+json_r[i][0].fields.oem_name+'</td><td>'+json_r[i][0].fields.oem_type+'</td><td><div class="btn-group"> <button type="button" class="btn btn-success" aria-haspopup="true" aria-expanded="false"> Edit </button><div class="btn-group"> <button type="button" class="btn btn-danger" aria-haspopup="true" aria-expanded="false"> Delete </button> </div></div></td></tr>'
      $("#result").append(textString);
  }
}

const Tables = () => {
  fetchDataAsync();
  return (
    // <!-- Begin Page Content -->
    <div class="container-fluid">

      {/* <!-- Page Heading --> */}
      <h1 class="h3 mb-2 text-gray-800">OEM - Database</h1>
      <p class="mb-4">DataTables is a third party plugin that is used to generate the demo table below. For more information about DataTables, please visit the <a target="_blank" href="https://datatables.net">official DataTables documentation</a>.</p>

      {/* <!-- DataTales Example --> */}
      <div class="card shadow mb-4">  
        <div class="card-header py-3">
          <h6 class="m-0 font-weight-bold text-primary">DataTables Example</h6>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
              <thead>
                <tr>
                  <th value="oem_id">OEM_ID</th>
                  <th value="oem_name">OEM Name</th>
                  <th value="oem_type">OEM Type</th>
                                   
                  <th value="">Action</th>  
                </tr>
              </thead>
              <tfoot>

              <tr>
                  <th value="oem_id">OEM_ID</th>
                  <th value="oem_name">OEM Name</th>
                  <th value="oem_type">OEM Type</th>
                                   
                  <th value="">Action</th>  
                </tr>

              </tfoot>
              <tbody id="result">
                

            
               
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
    // <!-- /.container-fluid -->
  )
}

export default Tables;