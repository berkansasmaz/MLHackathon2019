using System.Collections.Generic;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System;
using MLHackathonServer.Entity;
using MLHackathonServer.Web.Models;

namespace MLHackathonServer.Web
{
    [Route("api/v1/[controller]")]
    public class ApiController : DbController		 //TODO: SecureDb controllerla değiştir
    {
		private UserManager<MLUser> _userManager;
        public UserManager<MLUser> UserManager => _userManager ?? (UserManager<MLUser>)HttpContext?.RequestServices.GetService(typeof(UserManager<MLUser>));

		public Guid UserId{
			get
			{
				var userId = UserManager.GetUserId(User);
				return Guid.Parse(userId);
			}
		}

		[NonAction] // Bu non action belirtmezsek eğer asp.net bunu action olarak algılar ve .../Success miş gibi davranmasını sağlar.
		public IActionResult Success(string message = default(string), object data = default(object),object data2 = default(object), int code = 200){
			return Ok(
				new MLReturn(){
					Success = true,
					Message = message,
					Data = data,
					Code = code
				}
			); //Burada JSON' da dönebilirdim farketmez zaten döneceğim datadan o bunu anlıycak.
		}

		[NonAction]
		public IActionResult Error(string message = default(string), string internalMessage = default(string), object data = default(object), int code = 400, List<MLReturnError> errorMessage = null){
			var rv = new MLReturn(){
					Success = false,
					//User Message
					Message = message,
					//API User Message
					InternalMessage = internalMessage,
					Data = data,
					Code = code
				};
				
			if(rv.Code == 500)
				return StatusCode(500,rv);
			if(rv.Code == 401)
				return Unauthorized();
			if(rv.Code == 403)
				return Forbid();
			if(rv.Code == 404)
				return NotFound(rv);

			return BadRequest(rv); 
		}
    }
} 