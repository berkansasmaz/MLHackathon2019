using System;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace MLHackathonServer.Entity
{
    public class MLDBContext : IdentityDbContext<MLUser, MLUserRole, Guid>
    {
                public MLDBContext(DbContextOptions options) : base(options)
        {
        }
    }
}